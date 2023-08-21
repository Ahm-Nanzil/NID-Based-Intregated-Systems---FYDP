from django.contrib import admin
from django.urls import path
from meditech import views

urlpatterns = [
    path("", views.index, name='home') ,
    path("doctorviewpatientreport", views.doctorvieewpatientreport, name='doctorvieewpatientreport'),
    path("doctor", views.doctor, name='doctor'),
    path("medication", views.medication, name='medication'),
    path("report", views.report, name='report'),
    path("newmedication", views.newmedication, name='newmedication'),
    path("patient", views.patient, name='patient'),
    path("phermacy", views.phermacy, name='phermacy'),
    path("diagonesis", views.diagonesis, name='diagonesis'),

      
]
