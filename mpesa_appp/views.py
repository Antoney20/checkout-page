from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import requests
# Create your views here.
from django.http import HttpResponse
from .models import Registration
def index(request):
    return HttpResponse('Welcome index')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful, login the user
            #login(request, user)
            return redirect('checkout')  # Replace 'checkout' with your desired redirect URL

        else:
            # Authentication failed, show login page with error message
            error_message = 'Invalid username or password'
            return render(request, 'mpesa_appp/login.html', {'error_message': error_message})

    else:
        # GET request, render the login page
        return render(request, 'mpesa_appp/login.html')

@login_required
def checkout(request):
    # Fetch the user's data from the database
    user = request.user
    # Access the user's fields
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
    phone_number = user.phone_number
    profile_image = user.profile_image
    return render(request, 'mpesa_appp/Checkout.html')

def register(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')
        
        user = User.objects.create_user(username=first_name, password=password)
    
        registration = Registration(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
            password=password,
            dob=dob,
            email=email,
            profile_image=profile_image,
        )

        registration.save() 
        return render(request, 'mpesa_appp/Checkout.html')

   
    else:
        return render(request, 'mpesa_appp/register.html')