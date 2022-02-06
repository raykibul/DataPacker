from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import SurveyorSerializer
from .models import Surveyor

class SurveyorViewSet(viewsets.ModelViewSet):
    queryset = Surveyor.objects.all().order_by('username')
    serializer_class = SurveyorSerializer