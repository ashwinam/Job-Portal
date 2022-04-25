from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmployeeRegistrationForm, EmployerRegistrationForm, LoginForm, NewUserRegistrationForm


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
    # template_name = 'accounts/login.html'
    template_name = None


class LogOut(LogoutView):
    template_name='accounts/logout.html'


def loginHandler(request):
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email, password)
            user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            print('login successfuly')
            return redirect('index')
        else:
            print('invalid credentials')
            return redirect('index')
    else:
        return HttpResponse('Not working')
        