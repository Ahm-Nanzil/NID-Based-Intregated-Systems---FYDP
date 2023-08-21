from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def doctorviewpatientreport(request):
    return render(request, 'doctor-view-patientreport.html')

def doctor(request):
    return render(request, 'doctor-view.html')
def medication(request):
    return render(request, 'view-medication.html')
def report(request):
    return render(request, 'view-report.html')
def newmedication(request):
    return render(request, 'new-medication.html')

def patient(request):
    return render(request, 'patient-view.html')
def phermacy(request):
    return render(request, 'phermacy-view.html')
def diagonesis(request):
    return render(request, 'diagonesis-view.html')