from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.NewUserRegistrationView.as_view(), name='newuser'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]
