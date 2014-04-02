from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'blog.views.posts'),
    url(r'^style/', 'blog.views.style'),
    url(r'^post/(?P<post_id>\d+)/', 'blog.views.post'),
    url(r'^post/likeme/(?P<post_id>\d+)/', 'blog.views.likeme'),
    url(r'^post/newcomment/(?P<post_id>\d+)/', 'blog.views.newcomment'),
    url(r'^login/', 'blog.views.login'),
    url(r'^logout/', 'blog.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    )