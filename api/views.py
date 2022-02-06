from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .serializer import Available_OptionsSerializer

# Create your views here.
def survey(request):
    survey=Available_Options.objects.all()
    options=Available_OptionsSerializer(survey)
    print(options.data)
    return(HttpResponse(options))