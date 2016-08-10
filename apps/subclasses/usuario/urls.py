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
from .views import EmployeeRegister, #EmployeeEdit, EmployeeList, EmployeeDetail, EmployeeDelete
##################################################


urlpatterns = (
	# EMPLOYEE URLS
	url(r'^dashboard/startup/register/$', login_required(EmployeeRegister.as_view()), name="startup-register"),
	#url(r'^dashboard/startup/list/$', login_required(EmployeeList.as_view()), name="startup-list"),
	#url(r'^dashboard/startup/detail/(?P<pk>\d+)/$', login_required(EmployeeDetail.as_view()), name="startup-detail"),
	#url(r'^dashboard/startup/edit/(?P<pk>\d+)/$', login_required(EmployeeEdit.as_view()), name="startup-edit"),
	#url(r'^dashboard/startup/delete/(?P<pk>\d+)/$', login_required(EmployeeDelete.as_view()), name="startup-delete"),
)
