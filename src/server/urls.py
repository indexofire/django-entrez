# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^favicon\.ico/$', RedirectView.as_view(url='%simg/favicon.ico' % settings.STATIC_URL)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entrez/', include('entrez.urls')),
    url(r'^room/', include('room.urls')),
    url(r'^account/', include('userena.urls'), name='account'),
    url(r'^social/', include('social_auth.urls')),
)

#urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT},
    ),
    url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'),
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT},
    ),
)
