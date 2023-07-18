from django.urls import path

from .import views

urlpatterns = [
    
    path('' , views.index, ),
    
    path('checkout' , views.checkout, name="checkout"),
    path('cart' , views.cart, name="cart"),
    path('register' , views.register, name="register"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('update/', views.update_item, name='update'),
    path('payment/', views.payment, name='payment'),
    
    
    
   # path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    #path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa_online'),
    
]