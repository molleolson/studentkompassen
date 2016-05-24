from django.forms import Form
from django.forms import inlineformset_factory, ModelForm, Textarea, DateField,CheckboxSelectMultiple, TextInput, MultipleChoiceField
from start.models import Event, Location, Host
from django.forms import inlineformset_factory, ModelForm,ChoiceField,RadioSelect,MultiWidget, CharField, DateField, TextInput
from start.models import Event, Host
from functools import partial
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget, DateWidget



class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name','categories','host', 'location', 'startdate', 'enddate', 'weekdays', 'description', 'description_english'
                  ]

        widgets = {
            # Use localization and bootstrap 3
            'startdate': DateTimeWidget(attrs={'class': 'DateTimeField'},
                                        options={'format': 'yyyy-mm-dd hh:ii'}, usel10n=False, bootstrap_version=3),
            'enddate': DateTimeWidget(attrs={'class':'DateTimeField'},
                                      options={'format': 'yyyy-mm-dd hh:ii'}, usel10n=False, bootstrap_version=3),
            'categories': CheckboxSelectMultiple(attrs={'class': 'choice_field'}),
            'weekdays': CheckboxSelectMultiple(attrs={'class': 'choice_field'}),
            'description': Textarea(attrs={'cols': 30, 'rows': 10}),
            'description_english': Textarea(attrs={'cols': 30, 'rows': 10}),
            'name': TextInput(attrs={'class': "nameofevent", 'rows':1}),


        }

        #MultipleChoiceField(required=True, widget=CheckboxSelectMultiple, choices='categories')

    def __init__(self, *args, **kwargs):
        allowed_hosts = kwargs.pop('allowed_hosts')
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['host'].queryset = Host.objects.filter(id__in=allowed_hosts)

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        startdate = cleaned_data.get('startdate')
        enddate = cleaned_data.get('enddate')
        if enddate < startdate:
            msg=u"End date must be after start date"
            self._errors['enddate'] = self.error_class([msg])

class PresentationForm(ModelForm):
    class Meta:
        model = Host
        fields = ['hostdescription', 'hostdescription_english']