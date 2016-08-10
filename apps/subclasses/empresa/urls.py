#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
##################################################

##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .views import StartupRegister
##################################################


urlpatterns = (
	url(r'^startup/register/$', login_required(StartupRegister.as_view()), name="startup-register"),
)
