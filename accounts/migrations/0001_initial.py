# Generated by Django 2.0.1 on 2018-04-14 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('part', 'Participant'), ('org', 'Organiser'), ('def', 'Default')], default='part', max_length=12)),
                ('phone', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('events_related', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]