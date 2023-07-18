from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from decimal import Decimal
#mpesa
import json
import requests
from django.http import HttpResponse, JsonResponse
from requests.auth import HTTPBasicAuth
from .backend import LipanaMpesa, MpesaAccessToken

# Create your views here.
from django.http import HttpResponse
from .models import Registration, Item,Order,OrderItem, Checkout


callback_url = "https://cd64-196-98-170-98.ngrok-free.app/app/v1/c2b/callback"

def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'mpesa_appp/index.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful, login the user
            login(request, user)
            return redirect('checkout')  # Replace 'checkout' with your desired redirect URL

        else:
            # Authentication failed, show login page with error message
            error_message = 'Invalid username or password'
            return render(request, 'mpesa_appp/login.html', {'error_message': error_message})

    else:
        # GET request, render the login page
        return render(request, 'mpesa_appp/login.html')
    

def logout_user(request):
    logout(request)
    return redirect('login') 
def cart(request):
    user = request.user
    orders = Order.objects.filter(username=user)
    order_items = OrderItem.objects.filter(order__in=orders)
    cart_items = sum(order.get_cart_items() for order in orders)
    cart_total = sum(order.get_cart_total() for order in orders)

  
    context = {
        'order_items': order_items,
        'orders' : orders,
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    print(context)
    return render(request, 'mpesa_appp/cart.html', context)

@login_required
def checkout(request):
    user = request.user
    orders = Order.objects.filter(username=user)
    order_items = OrderItem.objects.filter(order__in=orders)
    cart_items = sum(order.get_cart_items() for order in orders)
    cart_total = sum(order.get_cart_total() for order in orders)

  
    context = {
        'order_items': order_items,
        'orders' : orders,
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    print(context)
    return render(request, 'mpesa_appp/Checkout.html', context)



def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    user = request.user
    product = Item.objects.get(id=productId)
        # Retrieve the active (incomplete) order for the user
    order, created = Order.objects.filter(username=user, is_complete=False)
    # Retrieve or create the order item for the product and order
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=product)
    
    print(orderItem)
    
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    print('Product:', product)
    print('ProductId:', productId)
    print('Action:', action)
    
    return JsonResponse('Item was added/removed.', safe=False)


def register(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')
        
        user = Registration.objects.create_user(username=username, password=password)
    
        registration = Registration(
            username = username,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            password=password,
            email=email,
            profile_image=profile_image,
        )

        registration.save() 
        return render(request, 'mpesa_appp/Checkout.html')

   
    else:
        return render(request, 'mpesa_appp/register.html')
    

def payment(request):
    return HttpResposponse("payment")

def payment_details():
        # Assuming Checkout is the model representing the checkout table
    checkout_records = Checkout.objects.all()
        
    payment_details = []
    for record in checkout_records:
        phone_number = record.phone_number
        amount = record.amount
        payment_details.append({"phone_number": phone_number, "amount": amount})
        
    return payment_details
  