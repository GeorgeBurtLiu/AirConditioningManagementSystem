# Generated by Django 3.0.6 on 2020-06-28 01:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200628_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturesensor',
            name='last_update',
            field=models.TimeField(default=datetime.datetime(2020, 6, 28, 1, 50, 57, 306190), verbose_name='上次更新时间'),
        ),
    ]
