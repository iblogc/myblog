from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from blog import settings
from myblog.views import blog_list

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog_list, name='index'),
    url(r'^blog/', include('myblog.urls')),
    url(r'^say_something/', include('say_something.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
if settings.DEBUG is False:
    urlpatterns += patterns('',
                            url(r'^static/(?P<path>.*)$','django.views.static.serve',\
                            {'document_root': settings.STATIC_ROOT}),
                            )