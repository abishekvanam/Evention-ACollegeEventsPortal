from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Event
from logins.models import SignupData
from .forms import EventForm, NotificationForm
from .utility import send_whatsapp_message
import os
from selenium import webdriver

# Create your views here.
def about(request):
    return render(request, 'events/about.html')

def index(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})

def home(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/index.html', {'event_list': events})


def select_club(request):
    if request.method=='POST':
        club_name=request.POST.get('club_name')
        list_of_events=Event.objects.filter(club=club_name)
        return render(request,'events/display_events_under_club.html',{'list_of_events':list_of_events})
    else:
        return render(request,'events/select_club.html',{})
    pass




def detail_of_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id)
    return render(request,'events/detail.html',{'event':event})


def detail(request, slug):
    event = get_object_or_404(Event, tag=slug)
    participants = event.participants.all()
    return render(request, 'events/detail.html', {'event':event})


@login_required(login_url="logins:login_view")
def view_participants(request, slug):
    event = get_object_or_404(Event, tag=slug)
    participants = event.participants.all()
    return render(request,'events/participants_list.html', {'participants':participants})

#Creating an event
@login_required(login_url="logins:login_view")
def create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Event Created") #It is not rendered as it was not fitting with the template
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        pass
        #messages.error(request, "Could not create Event")
    return render(request, 'events/createform.html', {'form': form})

@login_required(login_url="logins:login_view")
def create_notification(request, slug):
    event = get_object_or_404(Event, tag=slug)
    title = 'Contact'
    form = NotificationForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        body = form.cleaned_data['body']
        subject = 'Message from  from event '
        print(subject)
        message = 'asfdfdf\n'
        send_whatsapp_message(message)
        title = "Success!"
        confirm_message = "All the participants of this events are notified."
        form = None
    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    return render(request, 'events/notifications.html', context)


#Updating an event
@login_required(login_url="logins:login_view")
def update(request, slug=None):
    event = Event.objects.get(tag=slug) #checking if logged in user is the organiser of the event
    organiser_of_event = event.organiser
    instance = get_object_or_404(Event, tag=slug)
    form = EventForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Event details updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        pass
        #messages.error(request, "Could not update Event")

    context = {
        'name' : instance.name,
        'description' : instance.description,
        'date' : instance.date,
        'organiser' : instance.organiser,
        'contact' : instance.contact,
        'form' : form,
        'organiser_of_event' : organiser_of_event,
    }
    return render(request, 'events/updateform.html', context)

@login_required(login_url="logins:login_view")
def delete(request, slug=None):
    event = Event.objects.get(tag=slug)
    organiser_of_event = event.organiser
    if request.user == organiser_of_event:
        instance = get_object_or_404(Event, tag=slug)
        instance.delete()
        messages.success(request, "Event deleted")
        return redirect('events:index')
    else:
        return render(request, 'events/delete.html')

def participate(request, slug):
    event = Event.objects.get(tag=slug)
    username = request.user
    current_user = SignupData.objects.get(user=username)
    event.participants.add(current_user)
    return render(request, 'events/success_participation.html',{})

def view_gallery(request, slug):
    event = get_object_or_404(Event, tag=slug)
    participants = event.participants.all()
    return render(request,'events/view_gallery.html', {'participants':participants, 'event':event})
