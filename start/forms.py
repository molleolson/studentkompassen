from django import forms
from django.forms import inlineformset_factory, ModelForm, DateField, TextInput
from start.models import Event, Location, Host
from functools import partial
from datetimewidget.widgets import DateTimeWidget


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'startdate', 'enddate', 'host', 'location']

        widgets = {
            # Use localization and bootstrap 3
            'startdate': DateTimeWidget(attrs={'class': "datetimepicker"}, usel10n=True, bootstrap_version=3),
            'enddate': DateTimeWidget(attrs={'class': "datetimepicker"}, usel10n=True, bootstrap_version=3)
            #'multipledates': DateTimeWidget(attrs={'class': "multidatespicker"}, usel10n=True, bootstrap_version=3),

        }


