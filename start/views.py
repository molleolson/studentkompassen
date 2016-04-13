from django.shortcuts import render
from django.http import HttpResponse
from .models import Host

def index(request):
    list_of_hosts = Host.objects.order_by('id')
    output = ', '.join([h.host_name for h in list_of_hosts])
    return HttpResponse(output)
# Create your views here.
def hostid(request, id):
    return HttpResponse("You're looking at host %s." % id)



