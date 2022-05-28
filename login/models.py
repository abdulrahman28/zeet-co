from django.db import models
from django.forms import CharField

# Create your models here.

class intel(models.Model):
    name = models.CharField(max_length=100)
    det = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    id = models.IntegerField(max_length=5,primary_key=True)

 
