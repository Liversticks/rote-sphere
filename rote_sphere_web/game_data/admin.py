from django.contrib import admin
from .models import Sensor, DayUsage, Profile

# Register your models here.
admin.site.register(Sensor)
admin.site.register(DayUsage)
admin.site.register(Profile)