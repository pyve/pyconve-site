# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Talk(models.Model):
    """
    """
    CHOICES = (
            (1, _('Talk')),
            (2, _('Workshop')),
            )

    title = models.CharField(_("Title"), blank=True, max_length=255)
    talk_type = models.IntegerField(_("Type"), choices=CHOICES)
    short_description = models.TextField(_("Description"))
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
