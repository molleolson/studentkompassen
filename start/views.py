from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse
from .models import Host, Event, Location
from start.forms import LocationForm, EventFormset
from django.template import loader

def index(request):

    hosts = Host.objects.all()
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

def addevent(request, id):

    form = LocationForm()
    event_formset = EventFormset(instance=Location())

    if request.POST:
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            event_formset = EventFormset(request.POST, instance=location)
            if event_formset.is_valid():
                event_formset.save()
            return redirect('/start/')

    return render_to_response('main.html',{
        'form': form, 'formset': event_formset
    },context_instance=RequestContext(request))


