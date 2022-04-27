from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

from .models import Employee
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
    template_name = 'accounts/login.html'


class LogOut(LogoutView):
    template_name='accounts/logout.html'
    success_url = '/'

"""
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
"""


class Profile(TemplateView):
    template_name = 'accounts/profile.html'

def profile(request):
    employee = Employee.objects.get(email=request.user)
    context = {'form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm, 'user':employee}
    return render(request, 'accounts/profile.html', context)