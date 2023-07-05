from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
from django.http import HttpResponse
from .models import Registration
def index(request):
    return HttpResponse('Welcome index')


@login_required
def checkout(request):
    # Fetch the user's data from the database
    user = request.user
    # Access the user's fields
    first_name = user.first_name
    middle_name = user.middle_name
    last_name = user.last_name
    email = user.email
    dob = user.dob
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