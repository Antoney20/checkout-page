from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse('Welcome index')
def checkout(request):
    return render(request, 'mpesa_appp/Checkout.html')
    