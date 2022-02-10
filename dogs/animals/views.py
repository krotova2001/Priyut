from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AnimalOne, Shelter
# Create your views here.

def index (request):
    template = loader.get_template('index.html')
    count_animals = AnimalOne.objects.all().count()
    animals = AnimalOne.objects.all
    context = {'animals': animals}
    return HttpResponse(template.render(context, request))