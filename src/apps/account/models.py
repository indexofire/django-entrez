# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(
        User,
        unique=True,
        verbose_name=_('user'),
        related_name='user_profile',
    )
    job = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.user.username
