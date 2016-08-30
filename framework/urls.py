#-*- coding: utf-8 -*-

##################################################
#				DJANGO IMPORTS                   #
##################################################
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.decorators import login_required
##################################################


'''
	DJANGO URLS
'''

urlpatterns = [
	url(r'^admin/', include('smuggler.urls')), 
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^i18n/', include('django.conf.urls.i18n'))
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

'''
	CUSTOM URLS
'''
urlpatterns += i18n_patterns(
	url(r'^$', login_required(RedirectView.as_view(url='framework/dashboard/home/'))),
	url(r'^framework/', include('apps.default.urls')),
	url(r'^framework/', include('apps.subclasses.empresa.startup.urls')),
	url(r'^framework/', include('apps.subclasses.usuario.employee.urls')),
)


'''
	MEDIA
'''
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
