from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse
from .models import Host, Event, Location
from start.forms import HostForm
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

def addevent(request):
    context=RequestContext(request)
#   form = LocationForm()
#    event_formset = EventFormset(instance=Location())

    if request.method == 'POST':
        form = HostForm(request.POST)                     # create a form instance and populate with data
        if form.is_valid():
            form.save(commit=True)
            #instance.host = Host.objects.get(name=offset)
            #instance.save()

            #event_formset = EventFormset(request.POST, instance=location)
            #if event_formset.is_valid():
            #   event_formset.save()

            return redirect('/start/addevent')
        else:
            print form.errors
    else:
        form = HostForm()

    return render_to_response('start/addevent.html', {'form': form}, context)


