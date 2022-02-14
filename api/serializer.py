from rest_framework import serializers

from .models import *

from users.models import NewUser

class SurveyorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewUser
        fields = ('user_name', 'zilla','upazilla','phoneNumber','name','email')
        
class Available_OptionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Available_Options
        fields = ('question_id','value','post_question')

class QuestionSerializer(serializers.ModelSerializer):
    available_options= Available_OptionsSerializer(many=True, read_only=True,source='available_options_set')
    class Meta:
        model = Question
        fields = ('question_text','answer_type','serial','image','survey_id','available_options')

class SurveySerializer(serializers.ModelSerializer):
    question_set=QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = Survey
        fields = ('id','name','question_set')


    
class Survey_InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey_Info
        fields = ('surveyor_id','surveyee_name','surveyee_phone','surveyee_address','survey_id')
class Survey_AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey_Answer
        fields = ('question_id','answer_value','survey_info_id')        
