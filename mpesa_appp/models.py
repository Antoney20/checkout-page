from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
    



class Registration(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profiles/')

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Item(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    item_image = models.ImageField(upload_to='item/images')

    def __str__(self):
        return self.name


####### mpesa payments.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True





