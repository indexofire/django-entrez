# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from entrez.models import EntrezEntry


class Room(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    creator = models.ForeignKey(User, related_name='creator')
    members = models.ManyToManyField(User, related_name='member')

    def __unicode__(self):
        return self.name


class RoomEntry(models.Model):
    room = models.ForeignKey(Room)
    entry = models.ForeignKey(EntrezEntry)
    link_time = models.DateTimeField()

    def __unicode__(self):
        return self.id
