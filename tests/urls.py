# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path(r"simple/", TemplateView.as_view(template_name="simple.html"), name="simple"),
    path(
        r"simple/strict_no_match/",
        TemplateView.as_view(template_name="simple_strict_no_match.html"),
        name="simple-strict-no-match",
    ),
    path(
        r"simple/custom-class/",
        TemplateView.as_view(template_name="simple_custom_class.html"),
        name="simple-custom-class",
    ),
    path(
        r"simple/settings-strict/",
        TemplateView.as_view(template_name="simple.html"),
        name="simple-settings-strict",
    ),
    path(
        r"simple/action/",
        TemplateView.as_view(template_name="simple_strict.html"),
        name="simple-action",
    ),
    path(
        r"detailed/action/<int:pk>/",
        TemplateView.as_view(template_name="detailed_action_kwargs.html"),
        name="detailed-action",
    ),
    path(
        r"detailed/action/not-active/<int:pk>/",
        TemplateView.as_view(template_name="detailed_action_kwargs_not_active.html"),
        name="detailed-action-not-active",
    ),
    path(
        r"detailed/action/multiple/<int:pk>/",
        TemplateView.as_view(template_name="detailed_action_kwargs_multiple.html"),
        name="detailed-action-multiple",
    ),
]
