from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import Employee, EmployeeProfile
from .forms import EmployeeRegistrationForm, EmployerRegistrationForm, LoginForm, NewUserRegistrationForm, UpdateProfileForm


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
    success_url = '/accounts/user-dashboard/'


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
    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm, 'user':employee}
    return render(request, 'accounts/profile.html', context)

def update_profile(request):
    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    return render(request, 'accounts/myprofile.html', context)

class UpdateProfile(UpdateView):
    model = EmployeeProfile
    form_class = UpdateProfileForm
    template_name = 'accounts/myprofile.html'
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = '/accounts/user-dashboard/'


class UpdateUserPassword(PasswordChangeView):
    template_name = 'accounts/password_update.html'
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = reverse_lazy('user-dashboard')

class UpdateUserPasswordDone(PasswordChangeDoneView):
    template_name = 'accounts/password_update_done.html'
