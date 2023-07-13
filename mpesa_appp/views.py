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
from .models import Registration, Item,Checkout


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

@login_required
def checkout(request):
    user = request.user
    # Access the user's fields
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    phone_number = user.phone_number
    profile_image = user.profile_image
    items = Item.objects.filter(user=user)
    
    total = 0

    for item in items:
        print(item.price)
        print(item.quantity)
        total += item.price * item.quantity
        total_cart = total
        

    #pass items to checkout
    context = {
        
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'profile_image': profile_image,
        'items': items,
        'amount':total_cart  
    }
    return render(request, 'mpesa_appp/Checkout.html', context)

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
  
def getAccessToken(request):
    consumer_key = 'jZZ1Izq3fr2ZB4jg0Kv6GAXy41G7d4ZG'
    consumer_secret = 'lghIvsY5Fkz7zXl3'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)

# Lipa na mpesa.  c2b
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}

    stk_request = {
        "BusinessShortCode": LipanaMpesa.Business_short_code,# this is the business shortcode
        "Password": LipanaMpesa.decode_password,
        "Timestamp": LipanaMpesa.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": payment_details.amount,
        "PartyA": payment_details.phone_number,
        "PartyB": LipanaMpesa.Business_short_code,
        "PhoneNumber":  payment_details.phone_number,  # replace with your phone number to get stk push
        "CallBackURL": callback_url,
        "AccountReference": "Antony",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=stk_request, headers=headers)
    return HttpResponse(response.text)

