from django.contrib import admin

from .models import Host, Event, Location

admin.site.register(Host)
admin.site.register(Event)
admin.site.register(Location)

# Register your models here.
