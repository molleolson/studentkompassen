from django.contrib import admin

from .models import Host, Event, Location, Category

admin.site.register(Host)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Category)

# Register your models here.
