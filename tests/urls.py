# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.urls import path
from django.views.generic import View

urlpatterns = [
    path(r"simple/", View.as_view(), name="simple"),
    path(r"multiple/", View.as_view(), name="multiple"),
    path(r"simple/action/", View.as_view(), name="simple-action"),
    path(r"multiple/action/", View.as_view(), name="multiple-action"),
    path(r"other/action/", View.as_view(), name="other-action"),
    path(r"detailed/action/<int:pk>/", View.as_view(), name="detailed-action"),
]
