from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'blog.views.style'),
    # url(r'^style/', 'blog.views.style'),
    url(r'^post/(?P<post_id>\d+)/', 'blog.views.post'),
    url(r'^post/likeme/(?P<post_id>\d+)/', 'blog.views.likeme'),
    url(r'^post/newcomment/(?P<post_id>\d+)/', 'blog.views.newcomment'),
    url(r'^login/', 'blog.views.login'),
    url(r'^logout/', 'blog.views.logout'),
    url(r'^register/', 'blog.views.register'),
    url(r'^admin/', include(admin.site.urls)),
    )