# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from myblog.models import Blog

__author__ = 'Korvin'


def sentence_index(request):
    sentences = Blog.objects.filter(is_delete=0, type=1).order_by('-publish_time')
    # tags = Tag.objects.all().order_by('-id')
    return render_to_response("say_something/index.html",
                              {"sentences": sentences},
                              context_instance=RequestContext(request))
