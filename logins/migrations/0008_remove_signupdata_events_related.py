# Generated by Django 2.0.3 on 2018-04-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0007_auto_20180414_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signupdata',
            name='events_related',
        ),
    ]
