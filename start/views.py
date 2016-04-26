from django.shortcuts import render, redirect, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Host, Event, Location
from start.forms import EventForm
from django.utils import translation
from django.template import loader
from django.contrib.auth import authenticate, login
from operator import attrgetter
from django.utils.translation import activate
from django.core.urlresolvers import reverse
from datetime import timedelta, datetime



def index(request):
    menu_active_item = 'now'
    events = Event.objects.filter(startdate__lt=datetime.now() + timedelta(days=1), enddate__gte=datetime.now())\
        .order_by('startdate')
    #events = sorted(temp, key=attrgetter('startdate'))
    #template = loader.get_template('start/main.html')
    #return HttpResponse(template.render(request))

    return render(request, 'start/main.html', locals())


#
#    output = ', '.join([h.host_name for h in list_of_hosts])
#     return HttpResponse(output)


def events(request):
    selected_date = datetime.strptime(request.GET.get('date'), "%Y-%m-%d")

    #print "Selected date", selected_date

    events = Event.objects.filter(startdate__lt=selected_date + timedelta(days=1), enddate__gte=selected_date)\
        .order_by('startdate')
    return render(request, 'start/events.html', locals())


def hostid(request, id):
    h = Host.objects.get(pk = id)
    return HttpResponse("You're looking at host %s." % h)


def about(request):
    menu_active_item = 'about'

   # if language == 'sv':
    #    translation.activate('sv')
   # elif language == 'en':
    #    translation.activate('en')
    return render(request, 'start/about.html', locals())


@login_required(login_url='/accounts/login')
def skapa(request, id):
    h = Host.objects.get(pk=id)
    #response = "Nu ska vi skapa ett event for host %h"
    return HttpResponse("Nu ska vi skapa ett event for %s" % h)


@login_required(login_url='/accounts/login')
def nationmain(request):
    menu_active_item = 'now'
    events = Event.objects.filter(startdate__lt=datetime.now() + timedelta(days=1), enddate__gte=datetime.now()) \
        .order_by('startdate')
    return render(request, 'start/nationmain.html', locals())

@login_required(login_url='/')
def studentmain(request):
    menu_active_item = 'now'
    events = Event.objects.filter(startdate__lt=datetime.now() + timedelta(days=1), enddate__gte=datetime.now()) \
        .order_by('startdate')
    return render(request, 'start/studentmain.html', locals())


@login_required(login_url='/accounts/login')
def ourevents(request):
    menu_active_item = 'ourevents'
    events = Event.objects.all().filter(host=1).order_by('startdate')
    return render(request, 'start/ourevents.html', locals())


@login_required(login_url='/accounts/login')
def presentation(request):
    menu_active_item = 'presentation'
    return render(request, 'start/presentation.html', locals())


@login_required(login_url='/accounts/login')
def addevent(request):

    menu_active_item = 'event'

    if request.method == 'POST':
        form = EventForm(request.POST)                     # create a form instance and populate with data

        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/start/nationmain/', locals())
    else:
        form = EventForm()

    return render(request, 'start/addevent.html', locals())


@login_required(login_url='/accounts/login')
def editevent(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.POST:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/start/nationmain/ourevents')
    else:
        form = EventForm(instance=event)

    return render(request, 'start/editevent.html', locals())
