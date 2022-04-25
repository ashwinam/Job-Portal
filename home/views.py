from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import LoginForm

def index(request):
    context = {'form':LoginForm}
    return render(request, "index.html", context)