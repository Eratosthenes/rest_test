# Generated by Django 2.1 on 2018-08-01 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='building',
            new_name='building_id',
        ),
    ]