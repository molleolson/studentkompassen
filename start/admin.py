from django.contrib import admin

from .models import Host, Event, Location, Category, Weekdays

admin.site.register(Host)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Weekdays)

# Register your models here.
