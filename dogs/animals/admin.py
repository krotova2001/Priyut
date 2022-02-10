from django.contrib import admin

# Register your models here.
from .models import AnimalOne, Shelter

admin.site.register(AnimalOne)
admin.site.register(Shelter)