# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.forms import ModelForm

from .models import Talk


class TalkCreateForm(ModelForm):
    class Meta:
        model = Talk
        exclude = ['approved']
        localized_fields = "__all__"
