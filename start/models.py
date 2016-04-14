from __future__ import unicode_literals
import datetime

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Host(models.Model):
    host_name = models.CharField(max_length=200)
    host_email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.host_name


class Event(models.Model):
    event_name = models.CharField(max_length=200, blank=True, null=True)
    event_description = models.CharField(max_length=400, blank=True, null=True)
    event_startdate = models.DateTimeField('start date')
    event_enddate = models.DateTimeField('end date')
    event_location = models.ForeignKey('Location', on_delete=models.CASCADE)
    #event_start_day = models.CharField(max_length=200, blank=True, null=True)           #Kanske ska va datum och ej string?
    #event_start_month = models.CharField(max_length=200, blank=True, null=True)
    #event_start_year = models.CharField(max_length=200, blank=True, null=True)
    #event_start_time = models.CharField(max_length=200, blank=True, null=True)
    #event_end_day = models.CharField(max_length=200, blank=True, null=True)
    #event_end_month = models.CharField(max_length=200, blank=True, null=True)
    #event_end_year = models.CharField(max_length=200, blank=True, null=True)
    #event_end_time = models.CharField(max_length=200, blank=True, null=True)

    #   event_participants = BooleanField(required = False)

    def __unicode__(self):
        return self.event_name

class Lunch(Event):
    lunch_menu = models.CharField(max_length=200) # Hr kanske vi sen kan testa lada in pdf?

class Other(Event):
    pass

class Location(models.Model):
    location_name = models.CharField(max_length=200, blank=True, null=True)
    location_gps = models.CharField(max_length=200, blank=True, null=True)
    location_street = models.CharField(max_length=200, blank=True, null=True)
    location_streetnumber = models.IntegerField(max_length=5, blank=True, null=True)
    location_zip = models.IntegerField(max_length=6, blank=True, null=True)
    location_city = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.event_name


class Admin(models.Model):
    admin_usrname = models.CharField(max_length=200)
#class Event(models.Model):