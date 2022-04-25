from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('signup/', views.EmployeeRegistrationView.as_view(), name='newuser'),
    # path('login/', views.LogIn.as_view(), name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', views.loginHandler, name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]
