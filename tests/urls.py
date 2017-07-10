# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.views.generic import View


urlpatterns = [
    url(r'^simple/$', View.as_view(), name='simple'),
    url(r'^simple/action/$', View.as_view(), name='simple-action'),
    url(r'^other/action/$', View.as_view(), name='other-action'),
]
