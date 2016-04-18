from django import forms
from django.forms import inlineformset_factory, ModelForm
from start.models import Event, Location, Host

#class LocationForm(ModelForm):
#    class Meta:
#        model = Location
 #       fields =('name', )


#EventFormset = inlineformset_factory(Location, Event, fields=('name', 'description', 'startdate',
#                                                              'enddate'), extra=1, can_delete=False)


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'startdate': forms.DateInput(attrs={'class': 'datepicker'}),
        }

