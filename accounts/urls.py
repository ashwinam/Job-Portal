from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('employeeSignup/', views.EmployeeRegistrationView.as_view(), name='emp_user'),
    path('employerSignup/', views.EmployerRegistrationView.as_view(), name='employer_user'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('password-update/', views.UpdateUserPassword.as_view(), name='update-password'),
    # path('password-update/done', views.UpdateUserPasswordDone.as_view(), name='password-change-done'),
    path('delete-user/<int:pk>', views.DeleteUser.as_view(), name="delete-user"),
    # path('profile/', views.Profile.as_view(), name='profile'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('my-profile/<int:pk>', views.UpdateProfile.as_view(), name="profile-update"),
    # path('my-profile/education/<int:pk>', views.InstitutionDetails.as_view(), name="education-detail"),
    path('my-profile/education/', views.institution_details, name="education-detail"),
    # path('login/', LoginView.as_view(), name='login'),
    # path('login/', views.loginHandler, name='login'),
]
