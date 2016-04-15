from __future__ import unicode_literals
import datetime

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Host(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    gps = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    streetnumber = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)


    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    startdate = models.DateTimeField('start date')
    enddate = models.DateTimeField('end date', )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    # event_start_day = models.CharField(max_length=200, blank=True, null=True)
    # Kanske ska va datum och ej string?
    # event_start_month = models.CharField(max_length=200, blank=True, null=True)
    # event_start_year = models.CharField(max_length=200, blank=True, null=True)
    # event_start_time = models.CharField(max_length=200, blank=True, null=True)
    # event_end_day = models.CharField(max_length=200, blank=True, null=True)
    # event_end_month = models.CharField(max_length=200, blank=True, null=True)
    # event_end_year = models.CharField(max_length=200, blank=True, null=True)
    # event_end_time = models.CharField(max_length=200, blank=True, null=True)

    #   event_participants = BooleanField(required = False)

    def __unicode__(self):
        return self.name


class Lunch(Event):
    menu = models.CharField(max_length=200) # Hr kanske vi sen kan testa lada in pdf?


class Other(Event):
    pass

class Cafe(Event):
    pass

class Breakfast(Event):
    pass

class Gasque(Event):
    dresscode = models.CharField(max_length=200)

class Club(Event):
    pass

class Pub(Event):
    pass

#class Administrator(models.Model):
#    username = models.CharField(max_length=200)
#class Event(models.Model):