# Generated by Django 3.1.2 on 2020-12-17 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_app', '0005_auto_20201115_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 12, 17, 13, 29, 8, 571725)),
        ),
    ]