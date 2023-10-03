from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import Appointment
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

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





def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')