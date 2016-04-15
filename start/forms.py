from django import forms
from django.forms import inlineformset_factory, ModelForm
from start.models import Event, Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


EventFormset = inlineformset_factory(Location, Event, fields=('name', 'description', 'startdate',
                                                              'enddate'), extra=1, can_delete=False)


