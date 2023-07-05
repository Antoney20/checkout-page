from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

