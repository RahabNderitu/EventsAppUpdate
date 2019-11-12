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
    maximum_tickets = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

class Ticket(models.Model):
    user_name = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    event= models.ForeignKey(Events,blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True)
    ticketid = models.IntegerField(null=True)


class Cart(models.Model):
    price = models.IntegerField(null=True)
    cartquantity= models.IntegerField(null=True)






  



























