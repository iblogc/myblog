# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from myblog.forms import BlogForm, TagForm
from myblog.models import Blog, Tag


def blog_list(request):
    blogs = Blog.objects.filter(is_delete=0, type=0).order_by('-publish_time')
    tags = Tag.objects.all().order_by('-id')
    return render_to_response("blog/blog_list.html",
                              {"blogs": blogs, "tags": tags},
                              context_instance=RequestContext(request))


def blog_show(request, id=''):
    blog = get_object_or_404(Blog, id=id)
    return render_to_response("blog/blog_show.html",
                              {"blog": blog},
                              context_instance=RequestContext(request))


def blog_filter(request, id=''):
    tags = Tag.objects.all().order_by('-id')
    tag = get_object_or_404(Tag, id=id)
    blogs = tag.blog_set.filter(is_delete=0)
    return render_to_response("blog/blog_list.html",
                              {"blogs": blogs, "tag": tag, "tags": tags},
                              context_instance=RequestContext(request))


@login_required
def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        tag = TagForm(request.POST)
        if form.is_valid() and tag.is_valid():
            cd = form.cleaned_data
            cdtag = tag.cleaned_data
            tagname = cdtag['tag_name']
            title = cd['caption']
            author = request.user
            content = cd['content']
            type = cd['type']
            blog = Blog(caption=title, author=author, content=content, type=type)
            blog.save()
            for taglist in tagname.split(','):
                Tag.objects.get_or_create(tag_name=taglist.strip())
                blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                blog.save()
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/blog/%s' % id)
    else:
        form = BlogForm()
        tag = TagForm()
    return render_to_response('blog/blog_add.html',
        {'form': form, 'tag': tag}, context_instance=RequestContext(request))


@login_required
def blog_update(request, id=""):
    blog = get_object_or_404(Blog, id=id)
    if request.user == blog.author:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            tag = TagForm(request.POST)
            if form.is_valid() and tag.is_valid():
                cd = form.cleaned_data
                cdtag = tag.cleaned_data
                tagname = cdtag['tag_name']
                tagnamelist = tagname.split(',')
                title = cd['caption']
                content = cd['content']
                # blog = get_object_or_404(Blog, id=id)
                if blog:
                    blog.caption = title
                    blog.content = content
                    blog.save()
                    for taglist in tagnamelist:
                        Tag.objects.get_or_create(tag_name=taglist.strip())
                        blog.tags.add(Tag.objects.get(tag_name=taglist.strip()))
                        blog.save()
                    tags = blog.tags.all()
                    for tagname in tags:
                        tagname = unicode(str(tagname), "utf-8")
                        if tagname not in tagnamelist:
                            notag = blog.tags.get(tag_name=tagname)
                            blog.tags.remove(notag)
                else:
                    blog = Blog(caption=blog.caption, content=blog.content)
                    blog.save()
                return HttpResponseRedirect('/blog/%s' % id)
        else:
            # blog = get_object_or_404(Blog, id=id)
            # form = BlogForm(initial={'caption': blog.caption, 'content': blog.content}, auto_id=False)
            form = BlogForm(instance=blog)
            tags = blog.tags.all()
            if tags:
                taginit = ''
                for x in tags:
                    taginit += str(x) + ','
                tag = TagForm(initial={'tag_name': taginit})
            else:
                tag = TagForm()
        return render_to_response('blog/blog_add.html',
                                  {'blog': blog, 'form': form, 'id': id, 'tag': tag},
                                  context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse("bloglist"))


@login_required
def blog_del(request, id=""):
    blog = get_object_or_404(Blog, id=id, author=request.user)
    if blog:
        blog.is_delete = 1
        blog.save()
        return HttpResponseRedirect("/blog/index/")
    blogs = Blog.objects.filter(is_delete=0)
    return render_to_response("blog/blog_list.html", {"blogs": blogs})


def blog_show_comment(request, id=''):
    blog = Blog.objects.get(id=id)
    return render_to_response('blog/blog_comments_show.html', {"blog": blog})


def blog_search(request):
    query = request.GET.get('query', '')
    qs = query.split(' ')
    if qs:
        
        if len(qs) == 0:
            return HttpResponseRedirect(reverse('blog_list'))
        else:
            qset = (
                Q(is_delete=0) &
                Q(type=0) &
                Q(caption__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__tag_name__icontains=query)
            )
            results = Blog.objects.filter(qset)
                
    tags = Tag.objects.all()
    return render_to_response("blog/blog_list.html",
                              {"blogs": results, "tags": tags},
                              context_instance=RequestContext(request))