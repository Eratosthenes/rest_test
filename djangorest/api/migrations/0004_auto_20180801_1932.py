# Generated by Django 2.1 on 2018-08-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_building_capitalization_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='administration',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='insurance',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='management',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='marketing',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='payroll',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='repairs',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='taxes',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='building',
            name='utility',
            field=models.FloatField(default=0.0),
        ),
    ]
