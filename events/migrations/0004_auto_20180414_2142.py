# Generated by Django 2.0.3 on 2018-04-14 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180414_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 21, 42, 23, 706702)),
        ),
    ]
