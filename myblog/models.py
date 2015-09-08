#-*- coding:utf-8 -*-
from django.contrib.auth.models import User

from django.db import models


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True, verbose_name=u'标签')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    class Meta:
        db_table = 'tag'  #自定义表名
        verbose_name = "标签"  #后台管理界面显示名字
        verbose_name_plural = "标签"  #后台管理界面显示名字
    def __unicode__(self):
        return self.tag_name

# class Author(models.Model):
#     """docstring for Author"""
#     name = models.CharField( max_length=30, verbose_name=u'用户名')
#     email = models.EmailField(blank=True, verbose_name=u'邮箱')
#     website = models.URLField(blank=True,verbose_name=u'网址')
#     class Meta:
#         db_table = 'author'  #自定义表名
#         verbose_name = "用户"  #后台管理界面显示名字
#         verbose_name_plural = "用户"  #后台管理界面显示名字
#     def __unicode__(self):
#         return u'%s' % (self.name)


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50, verbose_name=u'标题')
    author = models.ForeignKey(User, editable=False, verbose_name=u'用户',)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    content = models.TextField(verbose_name=u'内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=u'发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    type = models.IntegerField(verbose_name=u'文章类型')
    is_delete = models.BooleanField(verbose_name=u'是否删除')

    class Meta:
        db_table = 'blog'  #自定义表名
        verbose_name = "文章"  #后台管理界面显示名字
        verbose_name_plural = "文章"  #后台管理界面显示名字

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)
