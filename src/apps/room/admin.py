# -*- coding: utf-8 -*-
from django.contrib import admin
from room.models import Room, RoomEntry


class RoomAdmin(admin.ModelAdmin):
    pass


class RoomEntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomEntry, RoomEntryAdmin)