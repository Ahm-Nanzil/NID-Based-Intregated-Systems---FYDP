from django.contrib import admin
from django.urls import path
from meditech import views

urlpatterns = [
   path("", views.index, name='home') ,
   path("appoinment", views.appoinment, name='appoinment') ,

      
]
