from django.shortcuts import render
# from django.template import loader
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import events
from events.models import Events
from django.urls import reverse_lazy
from .forms import EventsForm


# Create your views here.
def index(request): 
    # context = {
    #     'page': 'index',
    #     'coverHeading': 'Search Events'
    # }
    return render(request, 'events/login.html')
 
def forgotpassword(request):
    return render(request, 'events/forgotpassword.html') 


@login_required(login_url='/events/login')
def dashboard(request):
    return render(request, 'events/dashboard.html')

def register(request):
    return render(request, 'events/register.html')

def login(request):
    return render(request, 'events/login.html')
# def logout(request):
#     return render(request, 'events/login.html')
def createEvents(request):
    return render(request, 'events/createEvents.html')
def movies(request):
    return render(request, 'events/movies.html') 
def events(request):
    return render(request, 'events/events.html')
 
def deleteEvents(request):
    return render(request, 'events/deleteEvents.html')  
def eventList(request):
    all_objects= Events.objects.all()
    context= {'all_objects': all_objects}

    return render(request, 'events/eventList.html',context)        

def showform(request):
    form= EventsForm(request.POST)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'events/createEvents.html', context)
def updateEvents(request, pk):
    event= get_object_or_404(Events, pk=pk)
    form = EventsForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events/eventList.html')
    return render(request, 'events/updateEvents.html', {'event':event})


def deleteEvents(request, pk):  
    event= get_object_or_404(Events, pk=pk)
    if request.method == "POST":
       event.delete()
       return redirect('events/eventList.html')
    context= {'event': event }
    return render(request, 'events/deleteEvents.html',context)   

    # event= get_object_or_404(Events, pk=pk)  
    # event.delete()  
    # return render(request,'events/deleteEvents.html',{'object': event})


def eventDetails(request, pk):
    event= get_object_or_404(Events, pk=pk)    
    context= {'event': event }
    return render(request, 'events/eventDetails.html', context)    



# def updateEvents(request, event_id):
#     event_id = int(event_id)
#     try:
#         event_check = Events.objects.get(id = event_id)
#     except Events.DoesNotExist:
#         return redirect('eventList')
#     form = EventsForm(request.POST or None, instance = event_check)
#     if form.is_valid():
#        form.save()
#        return redirect('eventList')
#     return render(request, 'events/updateEvents.html', {'form':form})     
# None is so that it doesn't raise validation errors before a user has pressed the submit button and post so
 # that it retains the data that a user enters into the form after the submit button is pressed
def do_login(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name','')
        password = request.POST.get('password', '')
        # authenticate user account.
        user = auth.authenticate(request, username=user_name, password=password)
        if user is not None:
            # login user account.
            auth.login(request, user)
            response = HttpResponseRedirect('/events/dashboard')
            # set cookie to transfer user name to login success page.
            response.set_cookie('user_name', user_name, 3600)
            return response
        else:
            error_json = {'error_message': 'User name or password is not correct.'}
            return render(request, 'events/login.html', error_json)
            # return render(request, 'events/login.html')
    else:
        return render(request, 'events/login.html')
def do_register(request):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        user_email = request.POST.get('user_email')
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.

            if User.objects.filter(username=user_name).exists():
                error_json = {'error_text': 'User account exist, please register another one.'}
                return render(request, 'events/register.html', error_json)
            else:    
                user = get_user_model().objects.create_user(username=user_name, password=user_password, email=user_email)
                # update user object staff field value and save to db.
                if user is not None:
                    # user.is_staff = True
                    # save user properties in sqlite auth_user table.
                    user.save()
                # redirect web page to login page.
                response = HttpResponseRedirect('/events/login')
                # set user name, pasword and email value in session.
                request.session['user_name'] = user_name
                request.session['user_password'] = user_password
                request.session['user_email'] = user_email
                return response
        else:
            error_json = {'error_message': 'User name, password and email can not be empty.'}
            return render(request, 'events/register.html', error_json)
    else:
        return render(request, 'events/register.html')

def logout(request):
    auth.logout(request)
    return render(request,'events/login.html')
    

# class EventList(ListView):
#     model = Events

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the events
#         context['eventList'] = Events.objects.all()
#         return context

# class EventView(DetailView):
#     model = Events

# class CreateEvents(CreateView):
#     model = Events
#     fields = ['event_title', 'event_type', 'event_location', 
#     'event_description', 'event_start_date','event_start_time','event_end_date','event_end_time']
#     success_url = reverse_lazy('eventList')

# class UpdateEvents(UpdateView):
#     model = Events
#     fields = ['event_title', 'event_type', 'event_location', 
#     'event_description', 'event_start_date','event_start_time','event_end_date','event_end_time']
#     success_url = reverse_lazy('eventList')
   # we use reverse_lazy to prevent occurrence of an error when url is not loaded.
# class DeleteEvents(DeleteView):
#     model = Events
#     success_url = reverse_lazy('eventList')





















# def createEvent(request):
#     # dec vars
#     event_title = str(request.POST['event-title']).title()
#     event_type = str(request.POST['event-type'])
#     event_location = str(request.POST['event-location'])
#     event_description = str(request.POST['event-description'])
#     event_start_date = str(request.POST['event-start-date'])
#     event_start_time = str(request.POST['event-start-time'])
#     event_end_date = str(request.POST['event-end-date'])
#     event_end_time = str(request.POST['event-end-time'])
#     creator = request.user

#     # create event
#     Event.objects.create(
#         name=event_title,
#         event_type=event_type,
#         creator=creator,
#         location=event_location,
#         description=event_description,
#         start_date=event_start_date,
#         start_time=event_start_time,
#         end_date=event_end_date,
#         end_time=event_end_time
#     )

    # #create response
    # response = {
    #     'status': 'success',
    # }

    # # send reponse JSON
    # return JsonResponse(response)



# def register(request):
#     # dec vars
#     username = str(request.POST['username']).lower()
#     email = str(request.POST['email']).lower()
#     password = str(request.POST['password'])

#     # check if username or email is used
#     username_check = User.objects.filter(username=username)
#     email_check = User.objects.filter(email=email)

#     if username_check:
#         response = {
#             'status': 'fail',
#             'error_msg': 'username already in use'
#         }
#     elif email_check:
#         response = {
#             'status': 'fail',
#             'error_msg': 'email already in use'
#         }
#     elif len(password) < 8:
#         response = {
#             'status': 'fail',
#             'error_msg': 'password must be atleast 8 characters long'
#         }
#     else:
#         # creating a  user
#         user = User.objects.create_user(username, email, password)

#         # login user
#         login(request, user)

#         # create response
#         response = {
#             'status': 'success',
#         }

#     # send reponse JSON
#     return JsonResponse(response)

# def myEvents(request):
#     # Dec  Vars
#     user = request.user

#     # redirect to signin page if user not found
#     try:
#         events = Event.objects.filter(creator=user)
#     except TypeError:
#         return redirect('register')

#     context = {
#         'page': 'myEvents',
#         'coverHeading': 'My Events',
#         'events': events
#     }
#     return render(request, 'events/myEvents.html', context)


# def editEvent(request, event_id):
#     # Dec  Vars
#     event = get_object_or_404(Event, pk=event_id)
#     context = {
#         'page': 'editEvent',
#         'coverHeading': 'Edit Event',
#         'event': event
#     }
#     return render(request, 'events/editEvent.html', context)


# # AJAX




# def logoutUser(request):
#     # log out user
#     logout(request)

#     # send to home page
#     return redirect('index')


# def searchEvents(request):
#     # dec vars
#     event_search = json.loads(request.body)['event_search']

#     # filter for matching events and serialize for json
#     event_search_results = list(Event.objects.filter(
#         name__icontains=event_search
#     ).values(
#         'id',
#         'name',
#         'event_type',
#         'start_date',
#         'attendees'
#     ))

#     # create response
#     response = {
#         'status': 'success',
#         'event_search_results': event_search_results
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def eventDetails(request):
#     # get event
#     event_id = json.loads(request.body)['event_id']
#     event = get_object_or_404(Event, pk=event_id)

#     # serialize json
#     serialized_event = serializers.serialize('json', [event])

#     # create response
#     response = {
#         'status': 'success',
#         'event': serialized_event
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def eventJoin(request):
#     # get event
#     user_id = int(request.POST['user-id'])
#     event_id = int(request.POST['event-id'])
#     user = User.objects.get(pk=user_id)
#     event = Event.objects.get(pk=event_id)

#     # add user to event
#     event.attendees.add(user)

#     # get updated attendance count
#     attendance = event.attendees.all().count()

#     # create response
#     response = {
#         'status': 'success',
#         'attendance': attendance
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def createEvent(request):
#     # dec vars
#     event_title = str(request.POST['event-title']).title()
#     event_type = str(request.POST['event-type'])
#     event_location = str(request.POST['event-location'])
#     event_description = str(request.POST['event-description'])
#     event_start_date = str(request.POST['event-start-date'])
#     event_start_time = str(request.POST['event-start-time'])
#     event_end_date = str(request.POST['event-end-date'])
#     event_end_time = str(request.POST['event-end-time'])
#     creator = request.user

#     # create event
#     Event.objects.create(
#         name=event_title,
#         event_type=event_type,
#         creator=creator,
#         location=event_location,
#         description=event_description,
#         start_date=event_start_date,
#         start_time=event_start_time,
#         end_date=event_end_date,
#         end_time=event_end_time
#     )

#     # #create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def updateEvent(request, event_id):
#     # dec vars
#     event_title = str(request.POST['event-title']).title()
#     event_type = str(request.POST['event-type'])
#     event_location = str(request.POST['event-location'])
#     event_description = str(request.POST['event-description'])
#     event_start_date = str(request.POST['edit-event-start-date'])
#     event_start_time = str(request.POST['edit-event-start-time'])
#     event_end_date = str(request.POST['edit-event-end-date'])
#     event_end_time = str(request.POST['edit-event-end-time'])
#     event = get_object_or_404(Event, pk=event_id)

#     # Update Event
#     event.name = event_title
#     event.event_type = event_type
#     event.location = event_location
#     event.description = event_description

#     # only update new dates/times
#     if event_start_date:
#         event.start_date = event_start_date

#     if event_end_date:
#         event.end_date = event_end_date

#     if event_start_time:
#         event.start_time = event_start_time

#     if event_end_time:
#         event.end_time = event_end_time

#     # Save updated event
#     event.save()

#     # create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def removeEvent(request):
#     # dec vars
#     event_id = json.loads(request.body)['event_id']
#     event = get_object_or_404(Event, pk=event_id)

#     # delete event
#     event.delete()

#     # create response
#     response = {
#         'status': 'success',
#     }

#     # send reponse JSON
#     return JsonResponse(response)


# def searchSystems(request):
#     system_query = json.loads(request.body)['system_query']
#     results = list(SolarSystem.objects.filter(name__icontains=system_query).values('name')[:5])

#     # create response
#     response = {
#         'status': 'success',
#         'results': results
#     }

#     # send reponse JSON
#     return JsonResponse(response)



   
    





