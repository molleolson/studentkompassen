from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Host, Event, Location
from start.forms import HostForm
from django.template import loader
from django.contrib.auth import authenticate, login

def index(request):

    hosts = Host.objects.all()

    #template = loader.get_template('start/main.html')
    #return HttpResponse(template.render(request))
    return render(request, 'start/main.html', locals())


#    
#    output = ', '.join([h.host_name for h in list_of_hosts])
#     return HttpResponse(output)

def loginpage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render('/start/')
            # Redirect to a success page.
        else:
            return HttpResponse("Incorrect password or username")
            # Return a 'disabled account' error message

    else:
        return HttpResponse("Invalid login")
        # Return an 'invalid login' error message.



def hostid(request, id):
    h = Host.objects.get(pk = id)
    return HttpResponse("You're looking at host %s." % h)

def skapa(request, id):
    h = Host.objects.get(pk=id)
    #response = "Nu ska vi skapa ett event for host %h"
    return HttpResponse("Nu ska vi skapa ett event for %s" % h)

def addevent(request):
#   form = LocationForm()
#    event_formset = EventFormset(instance=Location())

    menu_active_item = 'event'

    if request.method == 'POST':
        form = HostForm(request.POST)                     # create a form instance and populate with data

        if form.is_valid():
            instance = form.save()




            #event_formset = EventFormset(request.POST, instance=location)
            #if event_formset.is_valid():
            #   event_formset.save()

            #return render(request, '/start/addevent.html', {'form': form})
            return HttpResponseRedirect('/start')

    else:
        form = HostForm()

    return render(request, 'start/addevent.html', locals())


