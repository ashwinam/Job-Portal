from dataclasses import fields
from .models import NewUser, Employee, Employer
from django.contrib.auth.forms import UserCreationForm


class NewUserRegistrationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = [
            'name',
            'email',
            'password1',
            'password2'
        ]

class EmployeeRegistrationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'password1',
            'password2'
        ]

class EmployerRegistrationForm(UserCreationForm):
    class Meta:
        model = Employer
        fields = [
            'name',
            'email',
            'password1',
            'password2'
        ]