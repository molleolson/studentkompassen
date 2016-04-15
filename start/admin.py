from django.contrib import admin

from .models import Host, Event, Location, Lunch

admin.site.register(Host)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Lunch)

# Register your models here.
