from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    