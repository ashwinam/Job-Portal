from django import forms
from .models import EmployeeProfile, NewUser, Employee, Employer
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


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = [
            'profile_pic',
            'phone',
            'age',
            'gender'
        ]