from django import forms

from .models import Events,Ticket

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = fields = ['event_title', 'event_type', 'event_location', 
     'event_description', 'event_start_date','event_end_date','event_start_time','event_end_time','picture','price','maximum_tickets']





class TicketForm(forms.ModelForm):

	class Meta:
		model = Ticket
		fields = ( 'user_name', 'event', 'quantity','ticketid')

		
			















