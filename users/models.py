from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #check user is identical or not
    email = models.EmailField(unique=True)
    #return user is applicant or recruiter
    is_recruiter = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    #abstract applicant and recruiter
    has_resume = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)

# Create your models here.
