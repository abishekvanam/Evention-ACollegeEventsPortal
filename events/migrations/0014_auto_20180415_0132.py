# Generated by Django 2.0.3 on 2018-04-14 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20180414_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.CharField(choices=[('swa', 'Swayam'), ('it', 'Dept. Of Information Technology'), ('swa', 'CSI'), ('swa', 'TFI')], default='it', max_length=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 15, 1, 32, 33, 473581)),
        ),
    ]
