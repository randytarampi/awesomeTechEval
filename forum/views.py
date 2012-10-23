# Create your views here.
from django.core.urlresolvers import reverse
from settings import MEDIA_ROOT, MEDIA_URL

#RABBLE RABBLE RABBLE RABBLE... ran into an issue and 4 hours was enough time to make me choose another product

from string import join
from PIL import Image as PImage
from os.path import join as pjoin

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from settings import MEDIA_ROOT, MEDIA_URL
from forum.models import *
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
#from forum.models import *

#def main(request):
    """Main listing."""
#    forums = Forum.objects.all()
#    return render_to_response("forum/list.html", dict(forums=forums, user=request.user))

#def forum(request, pk):
    """Listing of threads in a forum."""
#    threads = Thread.objects.filter(forum=pk).order_by("-created")
 #   threads = mk_paginator(request, threads, 20)
#    return render_to_response("forum/forum.html", add_csrf(request, threads=threads, pk=pk))



def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def thread(request, pk):
    """Listing of posts in a thread."""
    posts = Post.objects.filter(thread=pk).order_by("created")
    posts = mk_paginator(request, posts, 15)
    title = Thread.objects.get(pk=pk).title
    return render_to_response("forum/thread.html", add_csrf(request, posts=posts, pk=pk,
        title=title, media_url=MEDIA_URL))
