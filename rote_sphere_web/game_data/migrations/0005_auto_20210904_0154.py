# Generated by Django 3.2.7 on 2021-09-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_data', '0004_auto_20210904_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
