# Generated by Django 2.1 on 2018-08-01 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_building_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='capitalization_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
