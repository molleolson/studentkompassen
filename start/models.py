from __future__ import unicode_literals
import datetime

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Host(models.Model):
    host_name = models.CharField(max_length=200)
    host_email = models.CharField(max_length=200)

    def __str__(self):
        return self.host_name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=400)
    event_date = models.CharField(max_length=200)
    event_start = models.CharField(max_length=200)
    event_end = models.CharField(max_length=200)

class Lunch(Event):


#class Location(models.Model):


#class Event(models.Model):