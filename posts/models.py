from django.db import models
from accounts.models import Employer

# Create your models here.

class JobPost(models.Model):
    posted_by = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    opening = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)