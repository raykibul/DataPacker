import io
import json

from django.shortcuts import render
from django.db.models import Prefetch
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import NewUser

from .serializer import *
from .models import *
# Create your views here.
class SurveyorViewSet(APIView):
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

#JSONtoDB
@csrf_exempt
def saveAnswer(request):
    if request.method == 'POST':
        jsonData = request.body
        #stream = io.BytesIO(jsonData)
        #data = JSONParser().parse(stream)
        data=json.loads(jsonData)
        for answers in data['answers']:
            #print(answers)
            deserializedData = Survey_AnswerSerializer(data=answers)
            #print(deserializedData)
            if deserializedData.is_valid():
                #print("valid")
                deserializedData.save()
            else:
                return HttpResponse(JSONRenderer().render(deserializedData.errors), content_type='application/json')
        message = {'msg' : 'successfully synced'}
        jsonData = JSONRenderer().render(message)
        return HttpResponse(jsonData, content_type = 'application/json')
        
    serializer_class = Survey_AnswerSerializer                    
