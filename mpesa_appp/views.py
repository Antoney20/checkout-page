from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#mpesa
import json
import requests
from django.http import HttpResponse, JsonResponse
from requests.auth import HTTPBasicAuth
# Create your views here.
from django.http import HttpResponse
from .models import Registration, Item
def index(request):
    return render(request, 'mpesa_appp/test.html')

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
    print("*************")
    for item in items:
        print("Name:", item.name)
        print("username", item.user)
        print("Quantity:", item.quantity)
        print("Price:", item.price)
        print("**************")
    #pass items to checkout
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'profile_image': profile_image,
        'items': items 
    }
    print(profile_image)
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
    
    
    
def getAccessToken(request):
    consumer_key = 'jZZ1Izq3fr2ZB4jg0Kv6GAXy41G7d4ZG'
    consumer_secret = 'lghIvsY5Fkz7zXl3'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)