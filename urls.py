from django.urls import path
from django.conf.urls import url
# from . import views


app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.EventList.as_view(), name='event_list'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('login', views.login, name='login'),
    path('do_login', views.do_login, name='do_login'),
    path('do_register', views.do_register, name='do_register'),
    path('createEvents', views.createEvents, name='createEvents'),
    path('movies', views.movies, name='movies'),
    path('events', views.events, name='events'),
    path('view/<int:pk>', views.EventView.as_view(), name='event_view'),
    path('new', views.EventCreate.as_view(), name='event_new'),
    path('edit/<int:pk>', views.EventUpdate.as_view(), name='event_edit'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event_delete'),
    # as_view() provides a function-like entry to class-based views
    ]