from rest_framework import serializers

from .models import *

class SurveyorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surveyor
        fields = ('username', 'password','zilla','upazilla','phoneNumber','name')

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('id','name')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text','answer_type','serial','image','survey_id')
class Available_OptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Available_Options
        fields = ('question_id','value','post_question')        
class Survey_InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey_Info
        fields = ('surveyor_id','surveyee_name','surveyee_phone','surveyee_address','survey_id')
class Survey_AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey_Answer
        fields = ('question_id','answer_value','survey_info_id')        
