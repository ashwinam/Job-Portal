from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('employeeSignup/', views.EmployeeRegistrationView.as_view(), name='emp_user'),
    # path('login/', views.LogIn.as_view(), name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('employerSignup/', views.EmployerRegistrationView.as_view(), name='employer_user'),
    path('login/', views.loginHandler, name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]
