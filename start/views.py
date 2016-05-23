# -*- coding: utf-8 -*-
import sys
import codecs
koden=sys.stdin.encoding


from django.shortcuts import render, redirect, render_to_response, RequestContext, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Host, Event, Location
from django.db.models import Q
from start.forms import EventForm, PresentationForm
from django.utils import translation, timezone
from django.template import loader
from django.contrib.auth import authenticate, login
from operator import attrgetter
from django.utils.translation import activate
from django.core.urlresolvers import reverse
from datetime import timedelta, datetime

# I denna fil finns all kod som faktiskt gor nagot vid visning av sidor. Exempelvis har alla flikar pa /start/ varsin
# funktion. De flesta funktioner liknar varandra till stor del.


def index(request, category=None):
    if category is None:
        menu_active_item = 'now'
    else:
        menu_active_item = category
    today = datetime.now()
    delta = timedelta(days=1)
    todays_weekday = today.strftime('%A')

    event_test = Event.objects.filter(Q(startdate__lte=timezone.now() + delta), Q(enddate__gte=timezone.now()),
                         Q(weekdays__name__startswith=todays_weekday))

    if category is not None:
        if category == 'club':
            afterparty = 'släpp'
            event_test = event_test.filter(Q(categories__name__istartswith=category) | Q(categories__name__istartswith=afterparty))
        else:
            event_test = event_test.filter(categories__name__istartswith=category)

    if event_test.exists():
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__name__startswith=todays_weekday) |
            Q(weekdays__isnull=True)

        ).order_by('startdate')

    else:
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__isnull=True)
        ).order_by('startdate')

    if category is not None:
        if category == 'club':
            afterparty = 'släpp'
            events = events.filter(Q(categories__name__istartswith=category) | Q(categories__name__istartswith=afterparty))
        else:
            events = events.filter(categories__name__istartswith=category)

    return render(request, 'start/main.html', locals())


########### Inläsning via kalendern ###########
def events(request, category=None):

    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    delta = timedelta(days=1)
    selected_weekday = selected_date.strftime('%A')

    event_test = Event.objects.filter(Q(startdate__lte=selected_date + delta), Q(enddate__gte=selected_date),
                                      Q(weekdays__name__startswith=selected_weekday))

    if category != 'now':
        if category == 'club':
            afterparty = 'släpp'
            event_test = event_test.filter(
                Q(categories__name__istartswith=category) | Q(categories__name__istartswith=afterparty))
        else:
            event_test = event_test.filter(categories__name__istartswith=category)

    if event_test.exists():
        events = Event.objects.filter(
            Q(startdate__lt=selected_date + delta),
            Q(enddate__gte=selected_date),
            Q(weekdays__name__startswith=selected_weekday) |
            Q(weekdays__isnull=True)
        ).order_by('startdate')

    else:
        events = Event.objects.filter(
            Q(startdate__lt=selected_date + delta),
            Q(enddate__gte=selected_date),
            Q(weekdays__isnull=True)
        ).order_by('startdate')

    if category != 'now':
        if category == 'club':
            afterparty = 'släpp'
            events = events.filter(Q(categories__name__istartswith=category) | Q(categories__name__istartswith=afterparty))
        else:
            events = events.filter(categories__name__istartswith=category)

    return render(request, 'start/events.html', locals())


def nationinfo(request):
    menu_active_item = 'info'

    hosts = Host.objects.order_by('name')
    return render(request, 'start/nationinfo.html', locals())


#@login_required(login_url='/accounts/login')
def myprofile(request):
    menu_active_item = 'myprofile'
    events = Event.objects.filter(startdate__lt=timezone.now(), enddate__gte=timezone.now()) \
        .order_by('startdate')

    return render(request, 'start/myprofile.html', locals())


@login_required(login_url='/accounts/login')
def skapa(request, id):
    h = Host.objects.get(pk=id)
    #response = "Nu ska vi skapa ett event for host %h"
    return HttpResponse("Nu ska vi skapa ett event for %s" % h)


@login_required(login_url='/accounts/login')
def nationmain(request):
    menu_active_item = 'now'
    today = datetime.now()
    delta = timedelta(days=1)
    todays_weekday = today.strftime('%A')
    nationname = request.user.get_username()
    nbr = nationname.find("_")
    nationname = nationname[:(nbr)]

    event_test = Event.objects.filter(Q(startdate__lte=timezone.now() + delta), Q(enddate__gte=timezone.now()),
                                      Q(weekdays__name__startswith=todays_weekday))

    if event_test.exists():
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__name__startswith=todays_weekday) |
            Q(weekdays__isnull=True)

        ).order_by('startdate')

    else:
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__isnull=True)
        ).order_by('startdate')

    return render(request, 'start/nationmain.html', locals())


@login_required(login_url='/accounts/login')
def ourevents(request):
    username = request.user.get_username()
    nbr = username.find("_")
    nationname = username[:(nbr)]
    username = username[:(nbr)]
    activeHost = Host.objects.filter(name__startswith=username)
    menu_active_item = 'ourevents'
    events = Event.objects.all().filter(host=activeHost, enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/ourevents.html', locals())

@login_required(login_url='/accounts/login')
def reload_ourevents(request):
    username = request.user.get_username()
    nbr = username.find("_")
    username = username[:(nbr)]
    activeHost = Host.objects.filter(name__startswith=username)

    events = Event.objects.all().filter(host=activeHost).order_by('startdate')
    return render(request, 'start/events.html', locals())


@login_required(login_url='/accounts/login')
def presentation(request):
    menu_active_item = 'presentation'

    activenation = request.user.get_username()
    nbr = activenation.find("_")
    nationname = activenation[:(nbr)]

    #activehost = Host.objects.filter(name__startswith = nationname)
    activehost = get_object_or_404(Host, name__startswith=nationname)

    if request.method == 'POST':
        form = PresentationForm(request.POST, instance=activehost)
        if form.is_valid():
            instance = form.save()
            return redirect('/start/nationmain/')
    else:
        form = PresentationForm(instance=activehost)

    return render(request, 'start/presentation.html', locals())


@login_required(login_url='/accounts/login')
def addevent(request):
    nationname = request.user.get_username()
    nbr = nationname.find("_")
    nationname = nationname[:(nbr)]
    activeHost = Host.objects.get(name__startswith=nationname)

    menu_active_item = 'event'

    if request.method == 'POST':
        form = EventForm(request.POST, allowed_hosts=[activeHost.id])          # create a form instance and populate with data

        if form.is_valid():
            instance = form.save()
            return redirect('/start/nationmain/')
    else:
        form = EventForm(allowed_hosts=[activeHost.id])

    return render(request, 'start/addevent.html', locals())


@login_required(login_url='/accounts/login')
def editevent(request, event_id):
    nationname = request.user.get_username()
    nbr = nationname.find("_")
    nationname = nationname[:(nbr)]
    activeHost = Host.objects.get(name__startswith=nationname)
    event = get_object_or_404(Event, pk=event_id)
    if request.POST:
        form = EventForm(request.POST, allowed_hosts=[activeHost.id], instance=event)
        if form.is_valid():
            form.save()
            return redirect('/start/nationmain/ourevents')
    else:
        form = EventForm(allowed_hosts=[activeHost.id], instance=event)

    return render(request, 'start/editevent.html', locals())

