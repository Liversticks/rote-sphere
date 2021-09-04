from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import DayUsageSerializer, SensorSerializer
from .models import DayUsage, Sensor

# Create your views here.
def index(request):
    return HttpResponse("Hello World - game_data")

class DayUsageViewSet(viewsets.ModelViewSet):
    # TODO: modify to return based on query string or POST body
    queryset = DayUsage.objects.all()
    serializer_class = DayUsageSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer