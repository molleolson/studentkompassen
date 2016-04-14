from django.shortcuts import render
from django.http import HttpResponse
from .models import Host, Event
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


