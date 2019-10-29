from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static


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
    path('updateEvents/<int:pk>', views.updateEvents, name='updateEvents'),
    path('deleteEvents/<int:pk>', views.deleteEvents, name='deleteEvents'),
    path('eventDetails/<int:pk>', views.eventDetails, name='eventDetails'),
  
    ]








