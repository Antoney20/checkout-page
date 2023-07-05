from django.urls import path

from . import views

urlpatterns = [
    path('index' , views.index, name="index"),
    path('checkout' , views.checkout, name="checkout"),
    path('register' , views.register, name="register"),
]