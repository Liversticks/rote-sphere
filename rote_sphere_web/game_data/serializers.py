from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Sensor, DayUsage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class SensorSerializer(serializers.ModelSerializer):
    """
    
    id = serializers.UUIDField()
    type = serializers.CharField(max_length=64)
    """
    linked_user = UserSerializer(read_only=True)
    class Meta:
        model = Sensor
        fields = ('linked_user', 'id')
        #fields = ['id']
    

class DayUsageSerializer(serializers.ModelSerializer):
    linked_sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())
    class Meta:
        model = DayUsage
        #fields = ('day', 'water', 'power')
        fields = ['linked_sensor', 'day', 'water', 'power']