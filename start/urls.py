from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

    # Sorting for categories
    url(r'^breakfast/$', views.event_breakfast, name='breakfast'),
    url(r'^breakfast/reload/$', views.reload_breakfast, name='reloadbreakfast'),
    url(r'^lunch/$', views.event_lunch, name='lunch'),
    url(r'^lunch/reload/$', views.reload_lunch, name='reloadlunch'),
    url(r'^cafe/$', views.event_cafe, name='cafe'),
    url(r'^cafe/reload/$', views.reload_cafe, name='reloadcafe'),
    url(r'^pub/$', views.event_pub, name='pub'),
    url(r'^pub/reload/$', views.reload_pub, name='reloadpub'),
    url(r'^restaurang/$', views.event_restaurang, name='restaurang'),
    url(r'^restaurang/reload/$', views.reload_restaurang, name='reloadrestaurang'),
    url(r'^club/$', views.event_club, name='club'),
    url(r'^club/reload/$', views.reload_club, name='reloadclub'),
    url(r'^gasque/$', views.event_gasque, name='gasque'),
    url(r'^gasque/reload/$', views.reload_gasque, name='reloadgasque'),
    # End sorting for categories

    url(r'^events/$', views.events, name='events'),
    url(r'^nationmain/$', views.nationmain, name='nationmain'),
    url(r'^nationmain/addevent/$', views.addevent, name='addevent'),
    url(r'^nationmain/editevent/(?P<event_id>\d+)/$', views.editevent, name='editevent'),
    url(r'^nationmain/presentation/$', views.presentation, name='presentation'),
    url(r'^nationmain/ourevents/$', views.ourevents, name='ourevents'),
    url(r'^studentmain/about/$', views.about, name='about'),
    url(r'^nationinfo/$', views.nationinfo, name='nationinfo'),
    url(r'^myprofile/$', views.myprofile, name='myprofile'),


]




