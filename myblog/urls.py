# -*- coding:utf-8 -*-
__author__ = 'Korvin'

from django.conf.urls import *

urlpatterns = patterns(('myblog.views'),
    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
    url(r'^$', 'blog_list', name='bloglist'),
    url(r'^index/$', 'blog_list', name='bloglist'),
    url(r'^(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
    url(r'^add/$', 'blog_add', name='addblog'),
    url(r'^(?P<id>\w+)/update/$', 'blog_update', name='updateblog'),
    url(r'^(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
    url(r'^(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
    url(r'^search/$', 'blog_search', name='blogsearch'),
)