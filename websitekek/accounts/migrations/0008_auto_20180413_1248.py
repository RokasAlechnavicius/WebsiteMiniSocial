# Generated by Django 2.0 on 2018-04-13 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180413_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorlogging',
            name='error_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 13, 9, 48, 26, 252052, tzinfo=utc)),
        ),
    ]