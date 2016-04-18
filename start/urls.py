from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nationmain/$', views.nationmain, name='nationmain'),
    url(r'^(?P<id>[0-9]+)/skapa/$', views.skapa, name='skapa'),
    url(r'^addevent/$', views.addevent, name='addevent'),


]