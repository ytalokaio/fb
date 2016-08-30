from django.db import models
from apps.default.models import Empresa
from simple_history.models import HistoricalRecords

'''
	SUBCLASSE DE EXEMPLO
'''
class Startup(models.Model):
	id_startup = models.AutoField(primary_key=True)
	empresa = models.OneToOneField(Empresa, on_delete = models.CASCADE,related_name='startup_name')
	representante = models.CharField(max_length=150, default='', blank=True,null=True)
	logo = models.ImageField(upload_to='media/subclasses/empresa/', blank=True,null=True, verbose_name='Imagem')
	history = HistoricalRecords()
	def __str__(self):
		return self.id_empresa.nomefantasia
	def __unicode__(self):
		return unicode(self.id_empresa.nomefantasia)
