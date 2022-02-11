from django.shortcuts import render
from django.db.models import Prefetch
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import NewUser

from .serializer import *
from .models import *

class SurveyorViewSet(viewsets.ModelViewSet):
     def post(self,request):
        queryset = NewUser.objects.get(email=request.user.email)
        serializer_class = SurveyorSerializer
        return Response(serializer_class(queryset, many=False).data)
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().prefetch_related(Prefetch('question_set',queryset=Question.objects.prefetch_related(
               "available_options_set")))
               
    serializer_class = SurveySerializer
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
class Available_OptionsViewSet(viewsets.ModelViewSet):
    queryset = Available_Options.objects.all()
    serializer_class = Available_OptionsSerializer
class Survey_InfoViewSet(viewsets.ModelViewSet):
    queryset = Survey_Info.objects.all()
    serializer_class = Survey_InfoSerializer
class Survey_AnswerViewSet(viewsets.ModelViewSet):
    queryset = Survey_Answer.objects.all()
    serializer_class = Survey_AnswerSerializer                    
