# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id_startup', models.AutoField(primary_key=True, serialize=False)),
                ('representante', models.CharField(max_length=150, null=True, default='', blank=True)),
                ('logo', models.ImageField(upload_to='media/subclasses/empresa/', null=True, verbose_name='Imagem', blank=True)),
                ('empresa', models.OneToOneField(to='default.Empresa', related_name='startup_name')),
            ],
        ),
    ]
