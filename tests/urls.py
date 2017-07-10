# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from active_link.urls import urlpatterns as active_link_urls

urlpatterns = [
    url(r'^', include(active_link_urls, namespace='active_link')),
]
