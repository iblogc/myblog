# -*- coding:utf-8 -*-
__author__ = 'Korvin'

from django.conf.urls import *

urlpatterns = patterns(('say_something.sentence'),
    # name属性是给这个url起个别名，可以在模版中引用而不用担心urls文件中url的修改 引用方式为{% url bloglist %}
    url(r'^$', 'sentence_index', name='sentence_index'),
)