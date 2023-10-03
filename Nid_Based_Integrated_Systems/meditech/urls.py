from django.contrib import admin
from django.urls import path
from meditech import views

urlpatterns = [
   path("", views.index, name='home') ,
   path("appoinment", views.appoinment, name='appoinment') ,
   path("contact", views.appoinment, name='appoinment') ,
   path("login", views.login, name='login') ,
   path("signup", views.signup, name='signup') ,


      
]
