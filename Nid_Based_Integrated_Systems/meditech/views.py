from django.shortcuts import redirect, render
#from django.shortcuts import render
from django.http import JsonResponse
from .models import newMedication

# Create your views here.

def index(request):
    return render(request, 'index.html')
def doctorviewpatientreport(request):
    return render(request, 'doctor-view-patientreport.html')

def doctor(request):
    return render(request, 'doctor-view.html')
def medication(request):
    newmedication = newMedication.objects.all()
    return render(request, 'view-medication.html',{'newmedication':newmedication})
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
def Prescription(request):
    if request.method == 'POST':
        PatientNID = request.POST.get('patient_NID')
        PatientName = request.POST.get('patient_name')
        PatientAge = request.POST.get('patient_age')
        StartDate = request.POST.get('start_date')
        EndDate = request.POST.get('end_date')
        DiseaseType = request.POST.get('disease_type')
        Medication = request.POST.get('medications')

        prescription = newMedication(
            PatientNID=PatientNID,
            PatientName=PatientName,
            PatientAge=PatientAge,
            StartDate=StartDate,
            EndDate=EndDate,
            DiseaseType=DiseaseType,
            Medication=Medication
        )

        
        prescription.save()
       
       

        # After processing, you can return a JSON response indicating success.
        response_data = {'message': 'Your appointment request has been received successfully.'}
        return JsonResponse(response_data)
    else:
        
        return render(request, 'new-medication.html')