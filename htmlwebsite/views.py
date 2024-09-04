from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from htmlwebsite.models import PollAdmin
from django.views.generic import CreateView
from .models import EndUser
from django.contrib import messages


# Create your views here.

from django.shortcuts import render, redirect
from .models import PollAdmin

def home(request):
    if request.method == "POST":
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username, email, or mobile already exist in the database
        if PollAdmin.objects.filter(username=username).exists():
            username_error = "Username already exists!"
            return render(request, 'htmlwebsite/index.html', {'username_error': username_error})

        if PollAdmin.objects.filter(email=email).exists():
            email_error = "Email already exists!"
            return render(request, 'htmlwebsite/index.html', {'email_error': email_error})

        if PollAdmin.objects.filter(mobile=mobile).exists():
            mobile_error = "Mobile number already exists!"
            return render(request, 'htmlwebsite/index.html', {'mobile_error': mobile_error})

        # If none of the above checks fail, create a new PollAdmin object
        polladmin = PollAdmin(email=email, mobile=mobile, username=username, password=password)
        polladmin.save()
        
        return render(request, 'htmlwebsite/signup_success.html')
    
    return render(request, 'htmlwebsite/index.html')



def Login(request):
    if request.method == "POST":
        email = request.POST.get('login-email')
        username = request.POST.get('login-username')
        password = request.POST.get('login-password')
        
        user_exists = PollAdmin.objects.filter(email=email, username=username, password=password).exists()

        if user_exists:
            # Redirect to conduct_poll view after successful login
            return redirect('conduct_poll')

        else:
            return render(request, 'login.html', {'login_error': 'Invalid email, username, or password'})

    return render(request, 'htmlwebsite/login.html')

def AfterLogin(request):
    return render(request, 'index3.html')

def conduct_poll(request):
    return render(request, 'polls/conduct_poll.html')

class RegisterEndUserView(CreateView):
    model = PollAdmin
    template_name = 'endusers.html'
    fields = ['email', 'mobile', 'password', 'confirm_password']
    success_url = '/success/'  # Update with your actual success URL

    def form_valid(self, form):
        # Additional validation or processing can be done here if needed
        return super().form_valid(form)
    
def endusers_view(request):
    # You can add any additional context data you want to pass to the template
    context = {
        'title': 'End Users Registration',
        # Add more context data if needed
    }
    return render(request, 'htmlwebsite/endusers.html', context)


def enduser_registration(request):
    print("Reached enduser_registration view function")
    if request.method == 'POST':
        name = request.POST['name']
        unique_id = request.POST['unique_id']
        mobile = request.POST['mobile']

        # Check if the unique_id already exists in the database
        if EndUser.objects.filter(unique_id=unique_id).exists():
            messages.error(request, 'Unique ID already exists.')
            return redirect('endusers')  # Redirect back to the registration page

        # Create a new EndUser object and save it to the database
        enduser = EndUser(name=name, unique_id=unique_id, mobile=mobile)
        enduser.save()

        messages.success(request, 'Registration successful!')
        return redirect('polls:index')  # Redirect to the 'index' URL in the 'Polls' app after successful registration

    # Handle GET requests or other cases where the method is not POST
    return render(request, 'htmlwebsite/endusers.html') 


def register_user(request):
    # Handle registration form submission logic here
    # Redirect to the 'index' URL in the 'Polls' app
    return redirect('polls:index')


def user_info(request):
    end_users = EndUser.objects.all()  # Retrieve all end users from the database
    return render(request, 'htmlwebsite/user_info.html', {'end_users': end_users})
