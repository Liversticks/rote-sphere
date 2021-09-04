from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# adapted from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100)
    # ISO 3166 2-letter country code
    country = CountryField()
    # no validation
    mailcode = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Sensor(models.Model):
    def __str__(self):
        return str(self.id)
    
    linked_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    id = models.UUIDField(primary_key=True)
    # I hope appliance names don't get too long
    type = models.CharField('appliance/meter type', max_length=64, default='None')

class DayUsage(models.Model):
    def __str__(self):
        return f'{str(self.linked_user.username)} {str(self.day)} Water used: {str(self.water)} Power used: {str(self.power)}' 
    
    linked_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    day = models.DateTimeField('tracked day')
    water = models.DecimalField('water usage', default=0, max_digits=14, decimal_places=10)
    power = models.DecimalField('power + gas usage', default=0, max_digits=14, decimal_places=10)
    # TODO: track a monetary cost per day?