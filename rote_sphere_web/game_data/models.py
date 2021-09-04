from django.db import models
from django.conf import settings

# Create your models here.

class Sensor(models.Model):
    linked_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    id = models.UUIDField(primary_key=True, editable=False)

class DayUsage(models.Model):
    linked_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    day = models.DateTimeField('tracked day')
    water = models.DecimalField('water usage', default=0, max_digits=14, decimal_places=10)
    power = models.DecimalField('power + gas usage', default=0, max_digits=14, decimal_places=10)
    # TODO: track a monetary cost per day?