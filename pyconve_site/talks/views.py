# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import Talk


class TalkListView(LoginRequiredMixin, ListView):
    model = Talk
    
    # Se usará el título como campo slug para las búsquedas.
    slug_field = "title"
    slug_url_kwarg = "title"
