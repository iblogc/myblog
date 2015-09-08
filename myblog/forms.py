# -*- coding:utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea, Select
from myblog.models import Blog, Tag

__author__ = 'Korvin'


class BlogForm(ModelForm):
    class Meta:
        type_choice = (
            (0, u'文章'),
            (1, u'一句话的事儿')
        )
        model = Blog
        field = {'caption', 'content', 'blog_type'}
        widgets = {
            'caption': TextInput(attrs={'class': 'form-control', 'style': 'margin-top:20px', 'placeholder': '请输入标题'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': '请输入内容'}),
            'type': Select(choices=type_choice, attrs={'placeholder': '请选择文章类型'})
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        field = {'tag_name'}
        widgets = {
            'tag_name': TextInput(attrs={'class': 'tagsinput'}),
        }