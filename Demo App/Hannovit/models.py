from django.db import models

# Create your models here.

class User(models.Model):
    Name=models.CharField(max_length=100, blank=False)
    Pan_Number=models.CharField(max_length=20, blank=False)
    Age=models.IntegerField(blank=False)
    Gender=models.CharField(max_length=20, blank=False)
    Email_Add=models.CharField(max_length=100, blank=False)
