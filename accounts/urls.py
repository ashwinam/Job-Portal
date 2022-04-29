from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('employeeSignup/', views.EmployeeRegistrationView.as_view(), name='emp_user'),
    path('employerSignup/', views.EmployerRegistrationView.as_view(), name='employer_user'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('password-update/', views.UpdateUserPassword.as_view(), name='update-password'),
    # path('profile/', views.Profile.as_view(), name='profile'),
    path('user-dashboard/', views.profile, name='user-dashboard'),
    path('my-profile/<int:pk>', views.UpdateProfile.as_view(), name="profile-update"),
    # path('login/', LoginView.as_view(), name='login'),
    # path('login/', views.loginHandler, name='login'),
]
