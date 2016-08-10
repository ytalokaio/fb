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
from apps.default.models import Projeto, Usuario, Empresa, Logradouro, Endereco, TipoEmpresa, TipoTelefone, TelefoneEmpresa # MODELS
from .models import Funcionario # MODELS
from .forms import EmployeeRegisterForm
from apps.default.views import JSONResponseMixin
##################################################



'''
----------------------------------------
			EMPLOYEE METHODS
----------------------------------------
''' 

class EmployeeRegister(JSONResponseMixin,View):
	def get(self, request):
		form = EmployeeRegisterForm
		return render (request, 'subclasses/usuario/employee/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = EmployeeRegisterForm(request.POST,request.FILES)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			password = request.POST['password']
			tipo_usuario = request.POST['tipo_usuario']
			genero = request.POST['genero']
			data_nascimento = request.POST['data_nascimento']
			cpf = request.POST['cpf']
			rg = request.POST['rg']
			orgaoemissor = request.POST['orgaoemissor']
			foto = request.POST['foto']

			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numero = request.POST['numero']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			nickname = request.POST['nickname']

			
			if not nome:
				context['Nome'] = ' cannot be empty !'
			if not sobrenome:
				context['Sobrenome'] = ' cannot be empty !'
			if not email:
				context['E-mail'] = ' cannot be empty !'
			if not password:
				context['password'] = ' cannot be empty !'

			if not tipo_usuario:
				context['Tipo'] = ' cannot be empty !'
			if not genero:
				context['Genero'] = ' cannot be empty !'
			if not data_nascimento:
				context['Data de nascimento'] = ' cannot be empty !'
			if not cpf:
				context['CPF'] = ' cannot be empty !'
			if not rg:
				context['RG'] = ' cannot be empty !'
			if not orgaoemissor:
				context['Orgão'] = ' cannot be empty !'
			'''
			if not foto:
				context['error_msg'] = 'foto cannot be empty !'
			'''
			if not cep:
				context['CEP'] = ' cannot be empty !'
			if not rua:
				context['Rua'] = ' cannot be empty !'
			if not bairro:
				context['Bairro'] = ' cannot be empty !'
			if not cidade:
				context['Cidade'] = ' cannot be empty !'
			if not estado:
				context['Estado'] = ' cannot be empty !'
			if not pais:
				context['Pais'] = ' cannot be empty !'
			if not numero:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Complemento'] = ' cannot be empty !'
			if not pontoreferencia:
				context['Refêrencia'] = ' cannot be empty !'
			if not nickname:
				context['Nickname'] = ' cannot be empty !'

			if not context:

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.nome = nome
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numero
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				usuario = Usuario.objects.create_user(email, password)
				usuario.nome = nome
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nome +" "+sobrenome
				usuario.tipo_usuario = tipo_usuario
				usuario.genero = genero
				usuario.data_nascimento = data_nascimento
				usuario.cpf = cpf
				usuario.rg = rg
				usuario.orgaoemissor = orgaoemissor
				usuario.foto = foto
				usuario.id_endereco = id_endereco
				usuario.save()

				funcionario = Funcionario()
				funcionario.usuario = usuario
				funcionario.nickname =  nickname
				funcionario.save()

				return redirect(reverse_lazy("user-list"))

			else:
				form = EmployeeRegisterForm(request.POST)

		return render (request, 'subclasses/usuario/employee/register.html', {'form':form ,'context':context})


'''
----------------------------------------
			END EMPLOYEE METHODS
----------------------------------------
'''