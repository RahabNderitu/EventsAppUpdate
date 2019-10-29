from django import forms

from .models import Events

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = fields = ['event_title', 'event_type', 'event_location', 
     'event_description', 'event_start_date','event_end_date','picture']