from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import Appointment


# Create your views here.

def index(request):
    return render(request, 'index.html')

def appoinment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        message = request.POST.get('message')
# Create a new Appointment instance with the form data
        appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            date=date,
            department=department,
            doctor=doctor,
            message=message
        )

        # Save the appointment data to the database
        appointment.save()
       
        # Here, you can process the form data as needed.
        # For example, you can save it to a database, send an email, etc.

        # After processing, you can return a JSON response indicating success.
        response_data = {'message': 'Your appointment request has been received successfully.'}
        return JsonResponse(response_data)
    else:
        # Handle GET requests or render a template if needed.
        return render(request, 'appointment_form.html')

   

def contact(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new ContactSubmission instance and save it to the database
        submission = ContactSubmission(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        submission.save()

        # Here, you can process the form data as needed.
        # For example, you can send an email or perform any other required actions.

        # After processing, you can return a JSON response indicating success.
        response_data = {'message': 'Your message has been sent and saved. Thank you!'}
        return JsonResponse(response_data)
    else:
        # Handle GET requests or render a template if needed.
        return render(request, 'index.html')  # Replace 'contact_form.html' with your template name
