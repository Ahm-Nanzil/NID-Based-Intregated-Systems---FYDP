from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model from Django's auth module
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    message = models.TextField(blank=True)  # Make it optional

    def __str__(self):
        return self.name

