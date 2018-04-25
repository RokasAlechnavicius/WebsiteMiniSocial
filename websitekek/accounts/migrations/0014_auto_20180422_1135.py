# Generated by Django 2.0 on 2018-04-22 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180413_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlogging',
            name='error_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 22, 11, 35, 5, 197939)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phonenumber',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
