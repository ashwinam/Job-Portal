from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    context = {'form':AuthenticationForm}
    return render(request, "index.html", context)