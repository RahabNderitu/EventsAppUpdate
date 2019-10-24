from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
# Create your models here.
class Events(models.Model):
    event_title = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_description = models.TextField(max_length=100)
    event_start_time = models.TimeField(max_length=100)
    event_end_time = models.TimeField(max_length=100)
#     user=models.ForeignKey(User)
# event_date = models.DateTimeField('Event Date')


# def __str__(self):
#       return self.name
# # is used to define how you want to provide string output of your class.
# class Movies(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#     theatre = models.CharField(max_length=100)
#     event_start_date = models.DateField(max_length=100)
#     event_start_time = models.TimeField(max_length=100)
#     event_end_date = models.DateField(max_length=100)
#     event_end_time = models.TimeField(max_length=100)

# class EventTickets(models.Model):
#     name= models.CharField(max_length=100)   
#     description = models.CharField(max_length=100)
#     theatre = models.CharField(max_length=100)
#     event_start_date = models.DateField(max_length=100)
#     event_start_time = models.TimeField(max_length=100)
#     event_end_date = models.DateField(max_length=100)
#     event_end_time = models.TimeField(max_length=100)



