from rest_framework import serializers

from .models import Surveyor

class SurveyorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Surveyor
        fields = ('username', 'password','zilla','upazilla','phoneNumber','name')