from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
#    url(r'^(?P<language>\w+)/nationmain/$', views.nationmain, name='nationmain'),
 #   url(r'^(?P<language>\w+)/studentmain/$', views.studentmain, name='studentmain'),
  #  url(r'^(?P<language>\w+)/nationmain/addevent/$', views.addevent, name='addevent'),
   # url(r'^(?P<language>\w+)/nationmain/presentation/$', views.presentation, name='presentation'),
    #url(r'^(?P<language>\w+)/nationmain/ourevents/$', views.ourevents, name='ourevents'),
#    url(r'^(?P<language>\w+)/studentmain/about/$', views.about, name='about'),
 #   url(r'^(?P<language>\w+)/language/$', views.language, name='language'),

    url(r'^events/$', views.events, name='events'),
    url(r'^nationmain/$', views.nationmain, name='nationmain'),
    url(r'^studentmain/$', views.studentmain, name='studentmain'),
    url(r'^nationmain/addevent/$', views.addevent, name='addevent'),
    url(r'^(?P<question_id>[0-9]+)/nationmain/editevent/$', views.editevent, name='editevent'),
    url(r'^nationmain/presentation/$', views.presentation, name='presentation'),
    url(r'^nationmain/ourevents/$', views.ourevents, name='ourevents'),
    url(r'^studentmain/about/$', views.about, name='about'),
    url(r'^language/$', views.language, name='language'),
]




