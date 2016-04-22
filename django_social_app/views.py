from django.shortcuts import render, redirect, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
    return render(request, 'login.html')

#@login_required(login_url='/')
#def home(request):
#    return render_to_response('/start/studentmain')


def logout(request):
    auth_logout(request)
    return redirect('/start')