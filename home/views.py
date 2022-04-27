from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import EmployeeRegistrationForm, EmployerRegistrationForm, LoginForm

def index(request):
    context = {'form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    return render(request, "index.html", context)