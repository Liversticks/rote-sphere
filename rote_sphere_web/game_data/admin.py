from django.contrib import admin
from .models import Sensor, DayUsage

# Register your models here.
admin.site.register(Sensor)
admin.site.register(DayUsage)
