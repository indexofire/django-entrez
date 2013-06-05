# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
    GENDER = (
        (1, _(u'male')),
        (2, _(u'femail')),
        (3, _(u'unknow')),
    )
    user = models.OneToOneField(
        User,
        unique=True,
        verbose_name=_('user'),
        related_name='user_profile',
    )
    nickname = models.CharField(
        max_length=255,
        blank=True,
        null=False,
    )
    gender = models.PositiveSmallIntegerField(
        choices=GENDER,
        max_length=1,
        default=3,
    )
    job = models.CharField(
        max_length=255,
        blank=True,
        null=False,
    )

    def __unicode__(self):
        return self.user.username

    def save(self):
        super(UserProfile, self).save()
        if self.nickname is None:
            self.nickname = self.user.username
