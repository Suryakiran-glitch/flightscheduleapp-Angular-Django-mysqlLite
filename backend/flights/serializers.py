from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Schedule

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
     model = User
     fields = ('url','username','email')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


