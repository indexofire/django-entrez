# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from entrez.models import EntrezEntry, EntrezTerm
from entrez.forms import AddTermForm
from entrez.utils import get_current_date


def get_user_all_terms(request):
    return EntrezTerm.objects.filter(owner=request.user).select_related()


def get_user_all_entries(request):
    return EntrezEntry.objects.filter(owner=request.user).select_related()


@login_required()
def index(request):
    tpl = 'entrez/entrez_index.html'
    ctx = {}
    ctx["objects"] = get_user_all_entries(request)
    ctx["terms"] = get_user_all_terms(request)
    ctx["form"] = AddTermForm()

    return render_to_response(tpl, ctx, context_instance=RequestContext(request))


@login_required()
def term_list(request, slug):
    tp = 'entrez/entrez_term_list.html'
    # todo: permission to check other user's term
    term = EntrezTerm.objects.get(slug=slug)
    objects = EntrezEntry.objects.filter(term=term).select_related()
    terms = EntrezTerm.objects.filter(owner=request.user).select_related()
    form = AddTermForm()
    ct = {
        "objects": objects[:30],
        "terms": terms,
        "form": form,
    }
    return render_to_response(tp, ct, context_instance=RequestContext(request))


@csrf_exempt
def add_term(request):
    form_class = AddTermForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            term = EntrezTerm.objects.create(
                name=form.cleaned_data["name"],
                slug=form.cleaned_data["slug"],
                db=form.cleaned_data["db"],
                period=form.cleaned_data["period"],
                owner=request.user,
                term=form.cleaned_data["term"],
                creation_date=get_current_date(),
                lastedit_date=get_current_date(),
            )
            term.save()

    return HttpResponseRedirect(reverse('entrez-index', ))


@csrf_exempt
def mark_as_read(request):
    if request.method == "POST":
        entry = get_object_or_404(EntrezEntry, pk=request.POST.get('feed_item_id'))
        entry.read = True
        entry.save()

    return HttpResponse()
