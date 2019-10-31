from django import forms

from .models import Events,Guest

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = fields = ['event_title', 'event_type', 'event_location', 
     'event_description', 'event_start_date','event_end_date','event_start_time','event_end_time','picture']



class GuestForm(forms.ModelForm):
	
    class Meta:
        model = Guest
        fields = ( 'name', 'email', 'phone', 'number_of_seats', 'is_attending', 'message')




















