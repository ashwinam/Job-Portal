from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.JobPost.as_view(), name="job-post")
]
