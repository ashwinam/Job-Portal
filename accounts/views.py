from django.shortcuts import render
from django.views.generic import CreateView
from .forms import EmployeeRegistrationForm, EmployerRegistrationForm, NewUserRegistrationForm


# Create your views here.

class NewUserRegistrationView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = NewUserRegistrationForm
    success_url = '/'

class EmployeeRegistrationView(CreateView):
    template_name = 'signup.html'
    form_class = EmployeeRegistrationForm
    success_url = '/'

class EmployerRegistrationView(CreateView):
    template_name = 'signup.html'
    form_class = EmployerRegistrationForm
    success_url = '/'
