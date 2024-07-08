from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_date = models.DateField(auto_now_add=True)
    company_name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    logo = models.ImageField(upload_to='job_logos/', null=True, blank=True)

    def __str__(self):
        return self.title



    
    


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)
    
    

    



class UserProfile(models.Model):
    first_name = models.CharField(max_length=255,default='')
    last_name = models.CharField(max_length=255,default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(default='')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    qualification = models.CharField(max_length=255, default='') 
    skills = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)


    def __str__(self):
        return self.user.username



    
    
    