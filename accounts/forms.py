from dataclasses import fields
from django import forms
from .models import EmployeeProfile, NewUser, Employee, Employer, Institution, Experience
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

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = [
            'certificate_name',
            'institute_university_name',
            'start_date',
            'end_date',
            'percentage_cgpa'
        ]

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            'job_title',
            'is_current_job',
            'start_date',
            'end_date',
            'company_name',
            'job_location_city',
            'job_location_state',
            'job_location_country',
            'about_job_role'
        ]