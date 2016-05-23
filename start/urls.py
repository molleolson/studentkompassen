from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'index/([a-zA-Z]+)?/$', views.index, name='index_with_type'),


    url(r'^myprofile/$', views.myprofile, name='myprofile'),


    # End sorting for categories
    url(r'^events/$', views.events, name='events'),
    url(r'^events/([a-zA-Z]+)?/$', views.events, name='events_with_type'),
    url(r'^nationmain/$', views.nationmain, name='nationmain'),
    url(r'^nationmain/addevent/$', views.addevent, name='addevent'),
    url(r'^nationmain/editevent/(?P<event_id>\d+)/$', views.editevent, name='editevent'),
    url(r'^nationmain/presentation/$', views.presentation, name='presentation'),
    url(r'^nationmain/ourevents/$', views.ourevents, name='ourevents'),
    url(r'^nationinfo/$', views.nationinfo, name='nationinfo'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),


]




