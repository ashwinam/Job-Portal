from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import Employee, EmployeeProfile, Employer, EmployerProfile, NewUser
from .forms import EmployeeRegistrationForm, EmployerRegistrationForm, ExperienceForm, InstitutionForm, LoginForm, NewUserRegistrationForm, UpdateEmployeeProfileForm, UpdateEmployerProfileForm


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

def user_dashboard(request):
    employee = NewUser.objects.get(email=request.user)
    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm, 'user':employee}
    return render(request, 'accounts/user_dashboard.html', context)

def update_profile(request):
    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    return render(request, 'accounts/myprofile.html', context)

class UpdateEmployeeProfile(UpdateView):
    model = EmployeeProfile
    form_class = UpdateEmployeeProfileForm
    template_name = 'accounts/myprofile.html'
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = '/accounts/user-dashboard/'

class UpdateEmployerProfile(UpdateView):
    model = EmployerProfile
    form_class = UpdateEmployerProfileForm
    template_name = 'accounts/myemployerprofile.html'
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = '/accounts/user-dashboard/'

class UpdateUserPassword(PasswordChangeView):
    template_name = 'accounts/password_update.html'
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = reverse_lazy('user-dashboard')

class UpdateUserPasswordDone(PasswordChangeDoneView):
    template_name = 'accounts/password_update_done.html'


class DeleteUser(DeleteView):
    model = NewUser
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = reverse_lazy('index')


class DeleteEmployerUser(DeleteView):
    model = Employer
    extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
    success_url = reverse_lazy('index')


# class InstitutionDetails(CreateView):
#     template_name = 'accounts/institution.html'
#     form_class = InstitutionForm
#     context_object_name = "form_edu"
#     extra_context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm}
#     success_url = reverse_lazy('profile-update')

def institution_details(request):
    form_edu = InstitutionForm()
    if request.method == "POST":
        form_edu = InstitutionForm(request.POST)
        if form_edu.is_valid():
            marking = form_edu.save(commit=False)
            marking.employee = request.user
            form_edu.save()
            return redirect('user-dashboard')
    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm, 'form_edu':form_edu}
    return render(request, 'accounts/institution.html', context)


def experience_details(request):
    form_exp = ExperienceForm
    if request.method == "POST":
        form_exp = ExperienceForm(request.POST)
        if form_exp.is_valid():
            marking = form_exp.save(commit=False)
            marking.employee = request.user
            form_exp.save()
            return redirect('user-dashboard')

    context = {'login_form':AuthenticationForm, 'reg_form':EmployeeRegistrationForm, 'reg_employer_form':EmployerRegistrationForm, 'form_exp':form_exp}
    return render(request, 'accounts/experience.html', context)