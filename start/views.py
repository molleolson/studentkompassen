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


def index(request):
    menu_active_item = 'now'
    today = datetime.now()
    delta = timedelta(days=1)
    #events = Event.objects.filter(startdate__lte=timezone.now()+delta, enddate__gte=timezone.now()).order_by('startdate')


    todays_weekday = today.strftime('%A')

    if Event.objects.filter(Q(startdate__lte=timezone.now()+delta), Q(enddate__gte=timezone.now()), Q(weekdays__name__startswith=todays_weekday)).exists():
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__name__startswith=todays_weekday) |
            Q(weekdays__isnull=True)

        ).order_by('startdate')

    else:
        print 'hello world'
        events = Event.objects.filter(
            Q(startdate__lte=timezone.now() + delta),
            Q(enddate__gte=timezone.now()),
            Q(weekdays__isnull=True)
        ).order_by('startdate')



    return render(request, 'start/main.html', locals())


def events(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    delta = timedelta(days=1)
    selected_weekday = selected_date.strftime('%A')

    if Event.objects.filter(Q(startdate__lte=selected_date + delta), Q(enddate__gte=selected_date),
                            Q(weekdays__name__startswith=selected_weekday)).exists():

        events = Event.objects.filter(
            Q(startdate__lt=selected_date + delta),
            Q(enddate__gte=selected_date),
            Q(weekdays__name__startswith=selected_weekday) |
            Q(weekdays__isnull=True)
        ).order_by('startdate')

    else:
        print 'Hello World'
        events = Event.objects.filter(
            Q(startdate__lt=selected_date + delta),
            Q(enddate__gte=selected_date),
            Q(weekdays__isnull=True)
        ).order_by('startdate')


    return render(request, 'start/events.html', locals())


# Start category-stuff for student user #################################


def event_pub(request):
    menu_active_item = 'pub'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Pub',
                                  startdate__lt=timezone.now()+delta, enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/pub.html', locals())


def reload_pub(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Pub', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_breakfast(request):
    menu_active_item = 'breakfast'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Frukost', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/breakfast.html', locals())


def reload_breakfast(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Frukost', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_lunch(request):
    menu_active_item = 'lunch'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Lunch', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/lunch.html', locals())


def reload_lunch(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Lunch', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_cafe(request):
    menu_active_item = 'cafe'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Fika', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/cafe.html', locals())


def reload_cafe(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Fika', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_restaurang(request):
    menu_active_item = 'restaurang'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Restaurang', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/restaurang.html', locals())


def reload_restaurang(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Restaurang', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_club(request):
    menu_active_item = 'club'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Klubb', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/club.html', locals())


def reload_club(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Klubb', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_gasque(request):
    menu_active_item = 'gasque'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Gasque', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/gasque.html', locals())


def reload_gasque(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Gasque', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


def event_other(request):
    menu_active_item = 'other'
    delta = timedelta(days=1)
    events = Event.objects.filter(categories__name__startswith='Other', startdate__lt=timezone.now()+delta,
                                enddate__gte=timezone.now()).order_by('startdate')
    return render(request, 'start/other.html', locals())


def reload_other(request):
    selected_date = timezone.make_aware(datetime.strptime(request.GET.get('date'), "%Y-%m-%d"),
                                        timezone.get_default_timezone())
    #print "Selected date", selected_date
    events = Event.objects.filter(categories__name__startswith='Other', startdate__lt=selected_date + timedelta(days=1),
                                  enddate__gte=selected_date).order_by('startdate')
    return render(request, 'start/events.html', locals())


# End category-stuff for student user ########################

def about(request):
    menu_active_item = 'about'

   # if language == 'sv':
    #    translation.activate('sv')
   # elif language == 'en':
    #    translation.activate('en')
    return render(request, 'start/about.html', locals())


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
    delta = timedelta(days=1)
    nationname = request.user.get_username()
    nbr = nationname.find("_")
    nationname = nationname[:(nbr)]
    events = Event.objects.filter(startdate__lt=timezone.now()+delta, enddate__gte=timezone.now()) \
        .order_by('startdate')
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

