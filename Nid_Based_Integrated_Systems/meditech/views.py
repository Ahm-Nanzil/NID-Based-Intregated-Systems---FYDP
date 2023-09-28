from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse



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

        # Print the form data to the terminal
        print("Received Appointment Form Data:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Date: {date}")
        print(f"Department: {department}")
        print(f"Doctor: {doctor}")
        print(f"Message: {message}")

        # Here, you can process the form data as needed.
        # For example, you can save it to a database, send an email, etc.

        # After processing, you can return a JSON response indicating success.
        response_data = {'message': 'Your appointment request has been received successfully.'}
        return JsonResponse(response_data)
    else:
        # Handle GET requests or render a template if needed.
        return render(request, 'appointment_form.html')