from django import forms
from django.forms import inlineformset_factory, ModelForm, DateField, TextInput
from start.models import Event, Location, Host
from functools import partial



#class LocationForm(ModelForm):
#    class Meta:
#        model = Location
 #       fields =('name', )


#EventFormset = inlineformset_factory(Location, Event, fields=('name', 'description', 'startdate',
#                                                              'enddate'), extra=1, can_delete=False)

class EventForm(ModelForm):
    #startdate = DateField(widget=TextInput(attrs={'class':'datetimepicker'}))
    #enddate = DateField(widget=TextInput(attrs={'class': 'datetimepicker'}))

    class Meta:
        model = Event
        fields = ['name', 'description','startdate', 'enddate', 'host', 'location']
        widgets = {
            'startdate': forms.DateTimeInput(attrs={'class':'datetimepicker'}),
            'enddate': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),

        }

       # widget=forms.DateTimeInput
        #startdate = widget
        #enddate = widget


