# Generated by Django 3.2.7 on 2021-09-04 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('linked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DayUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(verbose_name='tracked day')),
                ('water', models.DecimalField(decimal_places=10, default=0, max_digits=14, verbose_name='water usage')),
                ('power', models.DecimalField(decimal_places=10, default=0, max_digits=14, verbose_name='power + gas usage')),
                ('linked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
