from __future__ import unicode_literals
import datetime

from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible





class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    gps = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    streetnumber = models.IntegerField(blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)


    def __unicode__(self):
        return self.name

class Host(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)


    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    startdate = models.DateTimeField('start date')
    enddate = models.DateTimeField('end date', )
    multipledates = models.DateTimeField('multiple dates')
    host = models.ForeignKey(Host, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

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

# class EventTime(models.Model):
#    Event_Time=models.DateTimeField()