from django import forms
from django.forms import inlineformset_factory, ModelForm, Textarea, DateField,CheckboxSelectMultiple, TextInput, MultipleChoiceField
from start.models import Event, Location, Host
from django.forms import inlineformset_factory, ModelForm,ChoiceField,RadioSelect,MultiWidget, CharField, DateField, TextInput
from start.models import Event, Host
from functools import partial
from datetimewidget.widgets import DateTimeWidget, DateWidget



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'categories','host', 'location', 'startdate', 'enddate', 'reccurrences', 'description']

        widgets = {
            # Use localization and bootstrap 3
            'startdate': DateTimeWidget(attrs={'class': 'DateTimeField'}, options={'format': 'dd/mm/yyyy hh:ii'}, usel10n=False, bootstrap_version=3),
            'enddate': DateTimeWidget(attrs={'class':'DateTimeField'},options={'format': 'dd/mm/yyyy hh:ii'}, usel10n=False, bootstrap_version=3),
            #'multipledates': DateTimeWidget(attrs={'class': "multidatespicker"}, usel10n=True, bootstrap_version=3),
            'categories': CheckboxSelectMultiple(attrs={'class': 'choice_field'}),
            'description': Textarea(attrs={'cols': 60, 'rows': 10}),
            'name': TextInput(attrs={'class': "nameofevent", 'rows':1}),


        }

        #MultipleChoiceField(required=True, widget=CheckboxSelectMultiple, choices='categories')

    def __init__(self, *args, **kwargs):
        allowed_hosts = kwargs.pop('allowed_hosts')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['host'].queryset = Host.objects.filter(id__in=allowed_hosts)


class PresentationForm(ModelForm):
    class Meta:
        model = Host
        fields = ['description']