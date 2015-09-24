# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # URL pattern for the TalkListView
    url(
        regex=r'^$',
        view=views.TalkListView.as_view(),
        name='list'
    ),
    url(
        regex=r'create/$',
        view=views.TalkCreateView.as_view(),
        name='create'
        ),

    url(
        regex=r'success/$',
        view=TemplateView.as_view(template_name='talks/talk_success.html'),
        name='success'
        ),
]
