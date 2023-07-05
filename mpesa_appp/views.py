from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
from .models import Registration
def index(request):
    return HttpResponse('Welcome index')
def checkout(request):
    return render(request, 'mpesa_appp/Checkout.html')

def register(request):
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name', '')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')
    
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

   
    else:
        return render(request, 'mpesa_appp/register.html')