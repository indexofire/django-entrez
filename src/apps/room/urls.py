# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns


urlpatterns = patterns('room.views',
    url(r'^$', 'index', name='room-index'),
    url(r'^(?P<id>\d+)/$', 'room_detail', name='room-detail'),
)
