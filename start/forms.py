from django import forms
from django.forms import inlineformset_factory, ModelForm, Textarea, DateField,CheckboxSelectMultiple, TextInput, MultipleChoiceField
from start.models import Event, Location, Host
from django.forms import inlineformset_factory, ModelForm, DateField, TextInput
from start.models import Event, Host
from functools import partial
from datetimewidget.widgets import DateTimeWidget



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'categories','host', 'location', 'startdate', 'enddate', 'description']

        widgets = {
            # Use localization and bootstrap 3
            'startdate': DateTimeWidget(attrs={'class': "datetimepicker"}, usel10n=True, bootstrap_version=3),
            'enddate': DateTimeWidget(attrs={'class': "datetimepicker"}, usel10n=True, bootstrap_version=3),
            #'multipledates': DateTimeWidget(attrs={'class': "multidatespicker"}, usel10n=True, bootstrap_version=3),
            'categories': CheckboxSelectMultiple(attrs={'class': "MultipleChoiceField"}),
            'description': Textarea(attrs={'cols': 60, 'rows': 10})
        }

        #MultipleChoiceField(required=True, widget=CheckboxSelectMultiple, choices='categories')



class PresentationForm(ModelForm):
    class Meta:
        model = Host
        fields = ['description']