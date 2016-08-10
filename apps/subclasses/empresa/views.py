#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import (HttpResponse,
                         HttpResponseForbidden,
                         HttpResponseBadRequest)
from django.forms import formset_factory
##################################################



##################################################
#				CUSTOM IMPORTS                   #
##################################################
from .forms import StartupRegisterForm
from apps.default.views import JSONResponseMixin
##################################################


'''
	Startup Functions
'''
class StartupRegister(JSONResponseMixin,View):
	def get(self, request):
		form = StartupRegisterForm
		return render (request, 'subclasses/empresa/startup/register.html', {'form':form})

'''
	END Startup Functions
'''
