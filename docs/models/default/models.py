from django.db import models
from django.utils import timezone

'''
	MODELAGEM INICIAL PADRÃO
'''

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=45)
    abreviacao = models.CharField(max_length=1)
    def __str__(self):
        return self.descricao

class Logradouro(models.Model):
	id_logradouro = models.AutoField(primary_key=True)
	cep = models.IntegerField()
	nome = models.CharField(max_length=100)
	bairro = models.CharField(max_length=45)
	cidade = models.CharField(max_length=20)
	estado = models.CharField(max_length=2)
	pais = models.CharField(max_length=45)
	def __str__(self):
		return self.nome

class Endereco(models.Model):
	id_endereco = models.AutoField(primary_key=True)
	id_logradouro = models.ForeignKey('Logradouro', on_delete=models.DO_NOTHING)
	numero = models.IntegerField()
	complemento = models.CharField(max_length=45)
	pontoreferencia = models.CharField(max_length=45)
	def __str__(self):
		return self.complemento
		
class TipoEmpresa(models.Model):
	id_tipo_empresa = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class Empresa(models.Model):
	id_empresa = models.AutoField(primary_key=True)
	id_endereco = models.ForeignKey('Endereco', on_delete=models.DO_NOTHING)
	id_tipo_empresa = models.ForeignKey('TipoEmpresa', on_delete=models.DO_NOTHING)
	razaosocial = models.CharField(max_length=100)
	nomefantasia = models.CharField(max_length=100)
	cnpj = models.IntegerField()
	verificada = models.BooleanField(default=True)
	ie = models.CharField(max_length=45)
	def __str__(self):
		return self.razaosocial

class TipoUsuario(models.Model):
	id_tipo_usuario= models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoRelacao(models.Model):
	id_tipo_relacao = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoRelacaoEmpresa(models.Model):
	id_tipo_relacao_empresa = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoDocumento(models.Model):
	id_tipo_documento = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class TipoTelefone(models.Model):
	id_tipo_Telefone = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	id_tipo_usuario = models.ForeignKey('TipoUsuario', on_delete=models.DO_NOTHING)
	id_endereco = models.ForeignKey('Endereco', on_delete=models.DO_NOTHING)
	id_genero = models.ForeignKey('Genero', on_delete=models.DO_NOTHING)
	nomecompleto = models.CharField(max_length=100)
	cpf = models.IntegerField()
	data_nascimento = models.DateTimeField(default=timezone.now)
	rg = models.IntegerField()
	orgaoemissor = models.CharField(max_length=45)
	foto = models.ImageField(upload_to="uploads/users")
	def __str__(self):
		return self.nomecompleto

class TelefoneUsuario(models.Model):
	id_telefone_usuario = models.AutoField(primary_key=True)
	id_tipo_telefone = models.ForeignKey('TipoTelefone', on_delete=models.DO_NOTHING)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
	numero = models.IntegerField()
	def __str__(self):
		return self.numero

class TelefoneEmpresa(models.Model):
	id_telefone_empresa = models.AutoField(primary_key=True)
	id_tipo_telefone = models.ForeignKey('TipoTelefone', on_delete=models.DO_NOTHING)
	id_empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING)
	numero = models.IntegerField()
	ramal = models.CharField(max_length=4)
	nome_contato = models.CharField(max_length=45)
	def __str__(self):
		return self.numero

class UsuarioEmpresa(models.Model):
	id_usuario_empresa = models.AutoField(primary_key=True)
	id_visao = models.ForeignKey('Visao', on_delete=models.DO_NOTHING)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
	id_empresa = models.ForeignKey('Empresa', on_delete=models.DO_NOTHING)
	ativo = models.BooleanField(default=True)
	def __str__(self):
		return self.ativo

class Visao(models.Model):
	id_visao = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=45)
	def __str__(self):
		return self.descricao

class RelacaoEmpresa(models.Model):
	id_relacao_empresa = models.AutoField(primary_key=True)
	id_empresa_1 = models.ForeignKey('TipoEmpresa', on_delete=models.DO_NOTHING)
	id_relacao_empresa = models.ForeignKey('TipoRelacaoEmpresa', on_delete=models.DO_NOTHING)
	data_criacao = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.criacao_data

class RelacaoUsuario(models.Model):
	id_relacao_usuario = models.AutoField(primary_key=True)
	id_usuario_1 = models.ForeignKey('TipoUsuario', on_delete=models.DO_NOTHING)
	id_tipo_relacao_empresa = models.ForeignKey('TipoRelacaoEmpresa', on_delete=models.DO_NOTHING)
	data_criacao = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.razaosocial

class Documento(models.Model):
	id_documento = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)
	id_tipo_documento = models.ForeignKey('TipoDocumento', on_delete=models.DO_NOTHING)
	anexo = models.ImageField(upload_to="uploads/documents")
	datahora = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.anexo