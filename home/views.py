from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import EmployeeRegistrationForm, EmployerRegistrationForm, LoginForm

def index(request):
    context = {'form':LoginForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    return render(request, "index.html", context)