from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    passWord = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)