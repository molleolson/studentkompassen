from django.contrib import admin

from .models import Host, Event, Location, Lunch, Other, Breakfast, Gasque,\
                    Cafe, Pub, Club

admin.site.register(Host)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Lunch)
admin.site.register(Other)
admin.site.register(Breakfast)
admin.site.register(Gasque)
admin.site.register(Cafe)
admin.site.register(Pub)
admin.site.register(Club)

# Register your models here.
