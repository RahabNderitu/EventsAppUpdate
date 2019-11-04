from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
# Create your models here.
class Events(models.Model):
    event_title = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='img/',default='')
    event_location = models.CharField(max_length=100)
    event_description = models.TextField(max_length=100)
    event_start_date = models.DateField(max_length=100)
    event_start_time = models.TimeField(max_length=100,null=True)
    event_end_date = models.DateField(max_length=100)
    event_end_time = models.TimeField(max_length=100 ,null=True)

class Guest(models.Model):
    name = models.CharField( max_length=50,blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50,blank=True,)
    number_of_seats = models.PositiveIntegerField(blank=True, null=True)
    is_attending = models.BooleanField(default=True)
    message = models.TextField(max_length=4000,blank=True)



class Ticket(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    ticket_type = models.CharField(max_length=20)
    quantity = models.IntegerField()
    total = models.IntegerField()
    event= models.ForeignKey(Events,on_delete=models.CASCADE)
    ticket= models.IntegerField()
    max_sellable_tickets= models.IntegerField()


    





























