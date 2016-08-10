from django.db import models

'''
	SUBCLASSE DE EXEMPLO
'''
class Funcionario(models.Model):
	id_funcionario = models.AutoField(primary_key=True)
	id_usuario = models.OneToOneField(Usuario, on_delete = models.DO_NOTHING, related_name='nome')
	nickname = models.CharField(max_length=20,null=True, blank=True)
	def __str__(self):
		return self.id_usuario.nome
	def __unicode__(self):
		return unicode(self.id_usuario.nome)