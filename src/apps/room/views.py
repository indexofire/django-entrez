# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from room.models import Room, RoomEntry


def index(request):
    tpl = 'room/room_list.html'
    ctx = {}
    ctx["rooms"] = Room.objects.all()
    return render_to_response(tpl, ctx, context_instance=RequestContext(request))


def room_detail(request, id):
    tpl = 'room/room_detail.html'
    ctx = {}
    ctx["room"] = Room.objects.get(id=id)
    ctx["members"] = ctx["room"].members.all()
    ctx["entries"] = RoomEntry.objects.filter(room=ctx["room"]).select_related()
    return render_to_response(tpl, ctx, context_instance=RequestContext(request))
    #if request.user.has_perm('can_view', room):
    #    ctx["entries"] = RoomEntry.objects.filter()
    #    render_to_response(tpl, ctx, context_instance=RequestContext(request))
    #else:
    #    raise
