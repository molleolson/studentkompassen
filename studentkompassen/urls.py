"""back-end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import start.views, django_social_app.views, django.contrib.auth.views
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import javascript_catalog

js_info_dict = {
    'packages': ('recurrence', 'dateAndTime', ),
}

urlpatterns = i18n_patterns(
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login', django.contrib.auth.views.login, ),
    url(r'^start/', include('start.urls', namespace="start")),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', django_social_app.views.login),
    url(r'^logout/$', django_social_app.views.logout),

)
