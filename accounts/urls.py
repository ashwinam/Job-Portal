from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.NewUserRegistrationView.as_view(), name='newuser')
]
