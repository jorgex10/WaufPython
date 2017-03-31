from django.contrib import admin
from apps.pet.models import Pet, Vaccine

# Register your models here.

admin.site.register(Pet)
admin.site.register(Vaccine)