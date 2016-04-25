from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),


    url(r'^nationmain/$', views.nationmain, name='nationmain'),
    url(r'^studentmain/$', views.studentmain, name='studentmain'),
    url(r'^nationmain/addevent/$', views.addevent, name='addevent'),
    url(r'^nationmain/presentation/$', views.presentation, name='presentation'),
    url(r'^nationmain/ourevents/$', views.ourevents, name='ourevents'),
    url(r'^studentmain/about/$', views.about, name='about'),

]




