from rest_framework import serializers
from .models import *
class Available_OptionsSerializer(serializers.Serializer):
    class Meta:
        model = Available_Options
        fields = ('value')