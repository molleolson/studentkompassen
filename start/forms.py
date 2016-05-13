from django import forms
from django.forms import inlineformset_factory, ModelForm, Textarea, DateField,CheckboxSelectMultiple, TextInput, MultipleChoiceField
from start.models import Event, Location, Host
from django.forms import inlineformset_factory, ModelForm,RadioSelect,MultiWidget, CharField, DateField, TextInput
from start.models import Event, Host
from functools import partial
from datetimewidget.widgets import DateTimeWidget, DateWidget



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'categories','host', 'location', 'startdate', 'enddate', 'reccurrences', 'description']

        dateTimeOptions= {

            'weekstart': '1',
            'todayBtn': True,
            'todayHighlight': True,
        }


        widgets = {
            # Use localization and bootstrap 3
            'startdate': DateTimeWidget(attrs={'class': 'DateTimeField', 'input_formats': '%m/%d/%y %H:%M'}, usel10n=True, bootstrap_version=3),
            'enddate': DateTimeWidget(attrs={'class':'DateTimeField'}, usel10n=True, bootstrap_version=3),
            #'multipledates': DateTimeWidget(attrs={'class': "multidatespicker"}, usel10n=True, bootstrap_version=3),
            'categories': CheckboxSelectMultiple(attrs={'class': 'choice_field'}),
            'description': Textarea(attrs={'cols': 60, 'rows': 10}),
            'name': TextInput(attrs={'class': "nameofevent", 'rows':1})

        }

        #MultipleChoiceField(required=True, widget=CheckboxSelectMultiple, choices='categories')



class PresentationForm(ModelForm):
    class Meta:
        model = Host
        fields = ['description']