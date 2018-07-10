from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from events.models import Event
# Create your models here.

class SignupData(models.Model):
    ACCOUNT_TYPE = (
        ('part', 'Participant'),
        ('org', 'Organiser'),
        ('def', 'Default'),
    )
    user= models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    #events_related = models.ManyToManyField(Event, unique=False, blank=True)
    first_name=models.CharField(max_length=150, null=True, blank=True)
    last_name=models.CharField(max_length=150, null=True, blank=True)
    user_type = models.CharField(max_length=12, choices=ACCOUNT_TYPE, default='def')
    email=models.EmailField(null=True, blank=True, unique=False, default='abc@example.com')
    phone_num=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
