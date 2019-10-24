from django.urls import path
from django.conf.urls import url
from . import views



app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('login', views.login, name='login'),
    path('do_login', views.do_login, name='do_login'),
    path('do_register', views.do_register, name='do_register'),
    path('createEvents', views.createEvents, name='createEvents'),
    path('movies', views.movies, name='movies'),
    path('events', views.events, name='events'),
    path("logout", views.logout, name="logout"),

    path('eventList', views.eventList, name='eventList'),
    path('forms', views.showform, name='forms'),
    # path('eventView', views.EventView.as_view(), name='eventView'),
    # path('eventView/<int:pk>', views.EventView.as_view(), name='eventView'),
    # path('createEvents', views.CreateEvents.as_view(), name='createEvents'),
    # path('new', views.EventCreate.as_view(), name='event_new'),
    # path('editEvents', views.UpdateEvents.as_view(), name='editEvents'),
    # path('deleteEvents', views.DeleteEvents.as_view(), name='deleteEvents'),
    # as_view() provides a function-like entry to class-based views
    ]