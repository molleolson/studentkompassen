from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Host, Event, Location
from start.forms import EventForm
from django.template import loader
from django.contrib.auth import authenticate, login
from operator import attrgetter


def index(request):
    menu_active_item = 'now'
    events = Event.objects.all().order_by('startdate')
    #events = sorted(temp, key=attrgetter('startdate'))
    #template = loader.get_template('start/main.html')
    #return HttpResponse(template.render(request))
    return render(request, 'start/main.html', locals())


#    
#    output = ', '.join([h.host_name for h in list_of_hosts])
#     return HttpResponse(output)


def hostid(request, id):
    h = Host.objects.get(pk = id)
    return HttpResponse("You're looking at host %s." % h)


def skapa(request, id):
    h = Host.objects.get(pk=id)
    #response = "Nu ska vi skapa ett event for host %h"
    return HttpResponse("Nu ska vi skapa ett event for %s" % h)


def nationmain(request):
    menu_active_item = 'now'
    events = Event.objects.all().order_by('startdate')
    return render(request, 'start/nationmain.html', locals())


def studentmain(request):
    menu_active_item = 'now'
    events = Event.objects.all().order_by('startdate')
    return render(request, 'start/studentmain.html', locals())


def presentation(request):
    menu_active_item = 'presentation'
    return render(request, 'start/presentation.html', locals())


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
