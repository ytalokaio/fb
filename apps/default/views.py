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
from .forms import LoginForm, RegisterForm # AUTH FORMS
from .forms import ProfileForm # PROFILE FORM
from .forms import UserRegisterForm # USER FORMS
from .forms import CompanyRegisterForm # COMPANY FORMS
from .forms import PhoneForm # PHONE FORMS
import requests
##################################################


'''
	CONVERT TO JSON
'''
class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


'''
----------------------------------------
			AUTH METHODS
----------------------------------------
'''
class Register(JSONResponseMixin,View):
	def get(self, request):
		form = RegisterForm
		return render (request, 'default/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = RegisterForm(request.POST)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			password = request.POST['password']
			
			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			if not sobrenome:
				context['error_msg'] = 'sobrenome cannot be empty !'
			if not email:
				context['error_msg'] = 'email cannot be empty !'
			if not password:
				context['error_msg'] = 'password cannot be empty !'

			if not context:
				user = Usuario.objects.create_user(email, password)
				user.nome = nome
				user.sobrenome = sobrenome
				user.save()
				return redirect(reverse_lazy("home"))

			else:
				form = RegisterForm()

		return render(request, 'default/register.html', {'form': form})


class Login(JSONResponseMixin,View):
	def get(self, request):
		form = LoginForm
		return render (request, 'default/login.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = LoginForm(request.POST)
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user is not None:
				login(request, user)
				return redirect(reverse_lazy("home"))
			else:
				context['error'] = True
				return render(request, 'default/login.html',{'form':form,'context':context})
		else:
		    form = LoginForm()

		return render(request, 'default/login.html', {'form': form})


class Logout(JSONResponseMixin, View):
	def get(self, request):
		logout(request)
		return redirect('/')


'''
----------------------------------------
			END AUTH METHODS
----------------------------------------
'''



'''
	DASHBOARD
'''
class Dashboard(JSONResponseMixin, View):
	def get(self, request):
		return render (request, 'default/dashboard.html')



'''
	DASHBOARD - PROFILE
'''
class Profile(JSONResponseMixin,UpdateView):
	form_class = ProfileForm
	template_name = 'default/profile.html'
	success_url = reverse_lazy("profile")

	def get_object(self, queryset=None):
		return self.request.user



'''
----------------------------------------
			USER METHODS
----------------------------------------
'''


class UserRegister(JSONResponseMixin,View):
	def get(self, request):
		form = UserRegisterForm
		return render (request, 'default/user/register.html', {'form':form})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = UserRegisterForm(request.POST)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			password = request.POST['password']

			
			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			if not sobrenome:
				context['error_msg'] = 'sobrenome cannot be empty !'
			if not email:
				context['error_msg'] = 'email cannot be empty !'
			if not password:
				context['error_msg'] = 'password cannot be empty !'

			

			if not context:			
				usuario = Usuario.objects.create_user(email, password)
				usuario.nome = nome
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nome +" "+sobrenome				
				usuario.save()

				return redirect(reverse_lazy("user-list"))

			else:
				form = UserRegisterForm()

		return render(request, 'default/user/register.html', {'form': form})


class UserEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		usuario = Usuario.objects.get(pk=pk)
		
		form = UserRegisterForm(
			initial={
			'nome': usuario.nome,
			'sobrenome': usuario.sobrenome,
			'email': usuario.email,			
			}
			)
		return render (request, 'default/user/edit.html', {'form':form})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = UserRegisterForm(request.POST)
			
			nome = request.POST['nome']
			sobrenome = request.POST['sobrenome']
			email = request.POST['email']
			
			if not nome:
				context['error_msg'] = 'nome cannot be empty !'
			if not sobrenome:
				context['error_msg'] = 'sobrenome cannot be empty !'
			if not email:
				context['error_msg'] = 'email cannot be empty !'

			if not context:				

				usuario = Usuario.objects.get(pk=pk)
				usuario.nome = nome
				usuario.sobrenome = sobrenome
				usuario.nomecompleto = nome +" "+sobrenome				
				usuario.save()

				return redirect(reverse_lazy("user-list"))

			else:
				form = UserRegisterForm()

		return render(request, 'default/user/edit.html', {'form': form})


class UserList(JSONResponseMixin,ListView):
	queryset = Usuario.objects.filter(is_admin=False)
	template_name = 'default/user/list.html'

	def get_context_data(self, **kwargs):
		context = super(UserList, self).get_context_data(**kwargs)
		return context


class UserDetail(JSONResponseMixin,DetailView):
	model = Usuario
	template_name = 'default/user/detail.html'

	def get_context_data(self, **kwargs):
		context = super(UserDetail, self).get_context_data(**kwargs)
		return context


class UserDelete(JSONResponseMixin,DeleteView):
	model = Usuario
	success_url = reverse_lazy('user-list')
	template_name = 'default/user/delete.html'


'''
----------------------------------------
			END USER METHODS
----------------------------------------
'''



'''
----------------------------------------
			COMPANY METHODS
----------------------------------------
'''
class CompanyRegister(JSONResponseMixin,View):
	def get(self, request):
		form = CompanyRegisterForm
		formset = formset_factory(PhoneForm)
		return render (request, 'default/company/register.html', {'form':form,'formset':formset})

	def post(self, request, *args, **kwargs):
		context = {}
		if request.method == 'POST':

			PhoneFormSet = formset_factory(PhoneForm)		
			formset = PhoneFormSet(request.POST, request.FILES)
			form = CompanyRegisterForm(request.POST)

						
			razaosocial = request.POST['razaosocial']
			nomefantasia = request.POST['nomefantasia']
			cnpj = request.POST['cnpj']
			verificada = request.POST.get('verificada', False)
			ie = request.POST['ie']
			id_tipo_empresa = request.POST['tipo_empresa']


			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numeroed = request.POST['numeroed']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']
			'''
			tipo_telefone = request.POST['tipo_telefone']
			numero = request.POST['numero']
			ramal = request.POST['ramal']
			nome_contato = request.POST['nome_contato']
			'''	
			if not razaosocial:
				context['Razão social'] = ' cannot be empty !'
			if not nomefantasia:
				context['Nome Fantasia'] = ' cannot be empty !'
			if not cnpj:
				context['CNPJ'] = ' cannot be empty !'			
			if not ie:
				context['IE'] = ' cannot be empty !'
			if not id_tipo_empresa:
				context['Tipo de Empresa'] = ' cannot be empty !'
			
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
			if not numeroed:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Comlemento'] = ' cannot be empty !'			
			
			listphones = []

			if formset.is_valid():
				for f in formset:
					phone = f.cleaned_data
					listphones.append([phone.get('tipo_telefone'),phone.get('numero'),phone.get('ramal'),phone.get('nome_contato')])

					if not phone.get('tipo_telefone'):
						context['Tipo Telefone'] = ' cannot be empty !'
					if not phone.get('numero'):
						context['Numero'] = ' cannot be empty !'
					if not phone.get('ramal'):
						context['Ramal'] = ' cannot be empty !'
					if not phone.get('nome_contato'):
						context['Contato'] = ' cannot be empty !'
						pass
			else:
				for erro in formset.errors:					
					context['error'] = erro
				pass

			
			

			if not context:

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.nome = rua
				id_logradouro.save()

				id_endereco = Endereco()
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numeroed
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				id_tipo_empresa = TipoEmpresa.objects.get(pk=id_tipo_empresa)

				empresa = Empresa()
				empresa.razaosocial = razaosocial
				empresa.nomefantasia = nomefantasia 
				empresa.cnpj = cnpj
				empresa.verificada = verificada
				empresa.ie = ie
				empresa.id_tipo_empresa = id_tipo_empresa				
				empresa.id_endereco = id_endereco
				empresa.save()

				for listphone in listphones:
					id_tipo_telefone = TipoTelefone.objects.filter(descricao=listphone[0])[0]			
					telempresa = TelefoneEmpresa()
					telempresa.id_tipo_telefone = id_tipo_telefone
					telempresa.id_empresa = empresa
					telempresa.numero = listphone[1]
					telempresa.ramal = listphone[2]
					telempresa.nome_contato = listphone[3]
					telempresa.save()
					
				return redirect(reverse_lazy("company-list"))

		else:
			form = CompanyRegisterForm()
			formset = formset_factory(PhoneForm)

		return render(request, 'default/company/register.html', {'form': form, 'formset':formset ,'context':context})


class CompanyEdit(JSONResponseMixin,View):
	def get(self, request, pk=None):
		empresa = Empresa.objects.get(pk=pk)
		telefone = TelefoneEmpresa.objects.filter(id_empresa=pk)[0]
		form = CompanyRegisterForm(
			initial={
			'razaosocial': empresa.razaosocial,
			'nomefantasia': empresa.nomefantasia,
			'cnpj': empresa.cnpj,
			'verificada': empresa.verificada,
			'ie': empresa.ie,
			'tipo_empresa': empresa.id_tipo_empresa,
			'cep' :  empresa.id_endereco.id_logradouro.cep,
		    'rua' :  empresa.id_endereco.id_logradouro.nome,
		    'bairro' :  empresa.id_endereco.id_logradouro.bairro,
		    'cidade' :  empresa.id_endereco.id_logradouro.cidade,
		    'estado' :  empresa.id_endereco.id_logradouro.estado,
		    'pais' : empresa.id_endereco.id_logradouro.pais,
		    'numeroed' :  empresa.id_endereco.numero,
		    'complemento' : empresa.id_endereco.complemento,
		    'pontoreferencia' :  empresa.id_endereco.pontoreferencia,
		    'tipo_telefone' : telefone.id_tipo_telefone,
			'numero' : telefone.numero,
			'ramal' : telefone.ramal,
			'nome_contato' : telefone.nome_contato,
		    
			}
			)

		return render (request, 'default/company/edit.html', {'form':form ,'telefone':  telefone})

	def post(self, request, pk=None, *args, **kwargs):
		context = {}
		if request.method == 'POST':		    
			form = CompanyRegisterForm(request.POST)
			
			razaosocial = request.POST['razaosocial']
			nomefantasia = request.POST['nomefantasia']
			cnpj = request.POST['cnpj']
			verificada = request.POST.get('verificada', False)
			ie = request.POST['ie']
			id_tipo_empresa = request.POST['tipo_empresa']


			cep = request.POST['cep']
			rua = request.POST['rua']
			bairro = request.POST['bairro']
			cidade = request.POST['cidade']
			estado = request.POST['estado']
			pais = request.POST['pais']

			numeroed = request.POST['numeroed']
			complemento = request.POST['complemento']
			pontoreferencia = request.POST['pontoreferencia']

			tipo_telefone = request.POST['tipo_telefone']
			numero = request.POST['numero']
			ramal = request.POST['ramal']
			nome_contato = request.POST['nome_contato']
								
			if not razaosocial:
				context['Razão social'] = ' cannot be empty !'
			if not nomefantasia:
				context['Nome Fantasia'] = ' cannot be empty !'
			if not cnpj:
				context['CNPJ'] = ' cannot be empty !'			
			if not ie:
				context['IE'] = ' cannot be empty !'
			if not id_tipo_empresa:
				context['Tipo de Empresa'] = ' cannot be empty !'
			
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
			if not numeroed:
				context['Número'] = ' cannot be empty !'
			if not complemento:
				context['Comlemento'] = ' cannot be empty !'
			if not pontoreferencia:
				context['Ponto de refêrencia'] = ' cannot be empty !'

			if not tipo_telefone:
				context['Tipo Telefone'] = ' cannot be empty !'
			if not numero:
				context['Numero'] = ' cannot be empty !'
			if not ramal:
				context['Ramal'] = ' cannot be empty !'
			if not nome_contato:
				context['Contato'] = ' cannot be empty !'

			if not context:

				empresa = Empresa.objects.get(pk=pk)
				id_endereco = Endereco.objects.filter(id_endereco=empresa.pk)[0]
				id_logradouro = Logradouro.objects.filter(id_logradouro=id_endereco.pk)[0]

				id_logradouro = Logradouro()
				id_logradouro.cep = cep
				id_logradouro.bairro = bairro
				id_logradouro.cidade = cidade
				id_logradouro.estado = estado
				id_logradouro.pais = pais
				id_logradouro.nome = rua
				id_logradouro.save()

				
				id_endereco.id_logradouro = id_logradouro
				id_endereco.numero = numeroed
				id_endereco.complemento = complemento
				id_endereco.pontoreferencia = pontoreferencia
				id_endereco.save()

				id_tipo_empresa = TipoEmpresa.objects.get(pk=id_tipo_empresa)
				
				empresa.razaosocial = razaosocial
				empresa.nomefantasia = nomefantasia 
				empresa.cnpj = cnpj
				empresa.verificada = verificada
				empresa.ie = ie
				empresa.id_tipo_empresa = id_tipo_empresa				
				empresa.id_endereco = id_endereco
				empresa.save()

				id_tipo_telefone = TipoTelefone.objects.get(pk=tipo_telefone)
				
				telempresa = TelefoneEmpresa.objects.filter(id_empresa=pk)[0]
				telempresa.id_tipo_telefone = id_tipo_telefone
				telempresa.id_empresa = empresa
				telempresa.numero = numero
				telempresa.ramal = ramal
				telempresa.nome_contato = nome_contato
				telempresa.save()

				return redirect(reverse_lazy("company-list"))

		else:
			form = CompanyRegisterForm()

		return render(request, 'default/company/edit.html', {'form': form,'context':context})


class CompanyList(JSONResponseMixin,ListView):
	model = Empresa
	template_name = 'default/company/list.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyList, self).get_context_data(**kwargs)
		return context      


class CompanyDetail(JSONResponseMixin,DetailView):
	model = Empresa
	template_name = 'default/company/detail.html'

	def get_context_data(self, **kwargs):
		context = super(CompanyDetail, self).get_context_data(**kwargs)
		return context


class CompanyDelete(JSONResponseMixin,DeleteView):
	model = Empresa
	success_url = reverse_lazy('company-list')
	template_name = 'default/user/delete.html'

'''
----------------------------------------
			END COMPANY METHODS
----------------------------------------
'''    


'''
----------------------------------------
			API'S INTEGRATION
----------------------------------------
'''
def get_cnpj_json(request):
	if request.method == 'GET':
		response = requests.get('http://receitaws.com.br/v1/cnpj/' + request.GET.get('cnpj')).json()
	return JsonResponse(response)

def get_cep_json(request):
	if request.method == 'GET':
		response = requests.get(
			'http://www.cepaberto.com/api/v2/ceps.json?cep=' + request.GET.get('cep'),
			headers={'Authorization': 'Token token=055cc8e8b0e25d6b6bb30a6dad8b1932'}
			).json()
	return JsonResponse(response)
