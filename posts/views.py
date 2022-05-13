from django.shortcuts import render
from django.views.generic import CreateView

from posts.forms import JobPostForm

# Create your views here.


class JobPost(CreateView):
    form_class = JobPostForm
    template_name = 'posts/jobposts.html'
    success_url = "/"