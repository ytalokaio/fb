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
from .views import EmployeeRegister
##################################################


urlpatterns = (
	url(r'^employee/register/$', login_required(EmployeeRegister.as_view()), name="employee-register"),
)