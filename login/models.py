from django.db import models

# Create your models here.


class detail(models.Model):
    uname = models.CharField(max_length=100)
    first = models.CharField(max_length=100,default='')
    other = models.CharField(max_length=100,default='')
    last = models.CharField(max_length=100,default='')
    dept = models.CharField(max_length=100,default='')
    faculty = models.CharField(max_length=100,default='')
    level = models.CharField(max_length=100,default='')
    gender = models.CharField(max_length=100,default='')
    name = models.CharField(max_length=100,default='')
    pword = models.CharField(max_length=100,default='')


