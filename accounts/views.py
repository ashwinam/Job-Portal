from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmployeeRegistrationForm, EmployerRegistrationForm, NewUserRegistrationForm


# Create your views here.

class NewUserRegistrationView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = NewUserRegistrationForm
    success_url = '/'

class EmployeeRegistrationView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = EmployeeRegistrationForm
    success_url = '/'

class EmployerRegistrationView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = EmployerRegistrationForm
    success_url = '/'


class LogIn(LoginView):
    template_name = 'accounts/login.html'


class LogOut(LogoutView):
    template_name='accounts/logout.html'