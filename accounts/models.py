from django.db import models
from events.models import Event
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    events_related = models.OneToOneField(Event, on_delete=models.CASCADE, null=True, unique=False, blank=True)
    ACCOUNT_TYPE = (
        ('part', 'Participant'),
        ('org', 'Organiser'),
        ('def', 'Default'),
    )
    user_type = models.CharField(max_length=12, choices=ACCOUNT_TYPE, default='part')
    phone = models.BigIntegerField(null=True, blank=True, unique=True)
    # is_organizer = models.BooleanField(default=False)
    # is_participant = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
