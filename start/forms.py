from django import forms
from django.forms import inlineformset_factory, ModelForm
from start.models import Event, Location, Host
from functools import partial

#class LocationForm(ModelForm):
#    class Meta:
#        model = Location
 #       fields =('name', )


#EventFormset = inlineformset_factory(Location, Event, fields=('name', 'description', 'startdate',
#                                                              'enddate'), extra=1, can_delete=False)

DateInput= partial(forms.DateTimeInput, {'class':'datepicker'})
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        startdate = forms.DateTimeInput(widgets=forms.DateTimeInput())
        enddate = forms.DateTimeInput(widgets=forms.DateTimeInput())

