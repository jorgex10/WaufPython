from django.db import models

# Create your models here.

class Person(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  dob = models.DateField()
  phone = models.CharField(max_length=9)
  email = models.EmailField()
  address = models.CharField(max_length=50)