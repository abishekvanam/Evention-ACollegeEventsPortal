from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.conf import settings
from django.db.models.signals import pre_save
from django.utils.timezone import now as timezone
from django.urls import reverse
import random, string
from . utility import unique_slug_generator

def upload_location(instance, filename):
    return '%s/%s' %(instance.tag, filename)

# Create your models here.
class Event(models.Model):

    CLUB_LIST = (
        ('Swayam', 'Swayam'),
        ('EcoClub', 'Eco Club'),
        ('ArtsClub', 'Arts club'),
        ('Abhinay', 'Abhinay'),
        ('ThemeBallet', 'Theme Ballet'),
        ('VCETalkies', 'Vasavi talkies'),
        # ('it', 'Dept. Of Information Technology'),
        ('CSI', 'CSI')
    )

    name = models.CharField(max_length = 32)
    tag = models.SlugField(max_length=50)

    club = models.CharField(max_length=12, choices=CLUB_LIST)#, default='it')

    description = models.TextField(default = '')
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=300)
    width_field = models.IntegerField(default=600)
    date = models.DateTimeField(default=datetime.now())
    organiser = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)#references to User model not UserProfile
    contact = models.EmailField(default="abc@gmail.com")
    participants = models.ManyToManyField('logins.SignupData', default=1, unique=False, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.tag:
            #if urltag is not existing create a unique url
            self.tag = unique_slug_generator(self)
        super(Event, self).save()

    def get_absolute_url(self):
        #to get url for events with slugs, since pk is not used
        return reverse("events:detail", kwargs={"slug": self.tag})


