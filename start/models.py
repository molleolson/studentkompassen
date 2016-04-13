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
    event_name = models.CharField(max_length=200, default=None)
    event_description = models.CharField(max_length=400, default=None)
    event_start_day = models.CharField(max_length=200, default=None)           #Kanske ska va datum och ej string?
    event_start_month = models.CharField(max_length=200, default=None)
    event_start_year = models.CharField(max_length=200, default=None)
    event_start_time = models.CharField(max_length=200, default=None)
    event_end_day = models.CharField(max_length=200, default=None)
    event_end_month = models.CharField(max_length=200, default=None)
    event_end_year = models.CharField(max_length=200, default=None)
    event_end_time = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.event_name

#class Lunch(Event):
  #  lunch_menu = models.CharField(max_length=200) # Hr kanske vi sen kan testa lada in pdf?



#class Location(models.Model):


#class Event(models.Model):