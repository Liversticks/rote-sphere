from rest_framework import serializers
from .models import Sensor, DayUsage

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        #fields = ('linked_user', 'id')
        fields = ('id', 'type')

class DayUsageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DayUsage
        fields = ('day', 'water', 'power')
        #fields = ('linked_user', 'day', 'water', 'power')