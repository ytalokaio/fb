#-*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Usuario, Projeto, Genero, Logradouro, Endereco, TipoEmpresa, Empresa, TipoUsuario, TipoRelacao, TipoRelacaoEmpresa, TipoDocumento, TipoTelefone, TelefoneUsuario, TelefoneEmpresa, UsuarioEmpresa,Visao, RelacaoEmpresa, RelacaoUsuario,Documento

from .forms import UserCreationForm, UserChangeForm

class ExampleAdmin(admin.ModelAdmin):
    change_list_template = 'smuggler/change_list.html'
    ...

class UserAdmin(BaseUserAdmin):
    # Formularios para adicionar ou alterar instancias dos usuarios
    form = UserChangeForm
    add_form = UserCreationForm

    # Os campos a serem no User model.
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('nome','sobrenome','foto','email', 'password',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # Campos a serem exibidos no cadastro de um usuario no painel admin.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Registra as alteracoes no painel admin
admin.site.register(Usuario, UserAdmin)
admin.site.register(Projeto, SimpleHistoryAdmin)
admin.site.register(Genero, SimpleHistoryAdmin)
admin.site.register(Logradouro, SimpleHistoryAdmin)
admin.site.register(Endereco, SimpleHistoryAdmin)
admin.site.register(TipoEmpresa, SimpleHistoryAdmin)
admin.site.register(Empresa, SimpleHistoryAdmin)
admin.site.register(TipoUsuario, SimpleHistoryAdmin)
admin.site.register(TipoRelacao, SimpleHistoryAdmin)
admin.site.register(TipoRelacaoEmpresa, SimpleHistoryAdmin)
admin.site.register(TipoDocumento, SimpleHistoryAdmin)
admin.site.register(TipoTelefone, SimpleHistoryAdmin)
admin.site.register(TelefoneUsuario, SimpleHistoryAdmin)
admin.site.register(TelefoneEmpresa, SimpleHistoryAdmin)
admin.site.register(UsuarioEmpresa, SimpleHistoryAdmin)
admin.site.register(Visao, SimpleHistoryAdmin)
admin.site.register(RelacaoEmpresa, SimpleHistoryAdmin)
admin.site.register(RelacaoUsuario, SimpleHistoryAdmin)
admin.site.register(Documento, SimpleHistoryAdmin)


admin.site.unregister(Group)
