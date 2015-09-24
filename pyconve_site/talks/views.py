# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse_lazy

from django.views.generic import CreateView
from django.views.generic import ListView

from braces.views import LoginRequiredMixin

from .models import Talk
from .forms import TalkCreateForm


class TalkListView(LoginRequiredMixin, ListView):
    model = Talk

    # Se usará el título como campo slug para las búsquedas en url.
    slug_field = "title"
    slug_url_kwarg = "title"


class TalkCreateView(CreateView):
    """ Vista que procesa el formulario para postular una nueva charla """
    model = Talk
    form_class = TalkCreateForm
    template_name = "talks/talk_create.html"

    success_url = reverse_lazy('talks:success')

    def form_valid(self, form):
        """
        Se debe implementar el envío de un correo al usuario
        informando que su propuesta será revisada y recibirá respuesta.
        """
        return super(TalkCreateView, self).form_valid(form)
