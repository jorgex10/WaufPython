from django.db import models
from apps.adoption.models import Person

# Create your models here.

class Vaccine(models.Model):
  name = models.CharField(max_length=50)

class Pet(models.Model):
  name = models.CharField(max_length=50)
  sex = models.CharField(max_length=10)
  dob = models.DateField()
  date_of_rescue = models.DateField()
  person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.CASCADE)
  vaccine = models.ManyToManyField(Vaccine, blank=True)