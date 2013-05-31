# -*- coding: utf-8 -*-
#from django.conf import settings
from django.contrib import admin
#from django.views.generic.base import RedirectView
from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^favicon\.ico/$', RedirectView.as_view(url='%s/img/favicon.ico' % settings.STATIC_URL), name='icon'),
    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()
"""
urlpatterns += patterns('',
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT},
    ),
    url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.strip('/'),
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT},
    ),
)
"""
