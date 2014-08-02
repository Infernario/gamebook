from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gamebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^users/', include('info.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/$', 'info.views.account'),
    url(r'^$', 'info.views.index'),
    url(r'^account/attending.html', 'info.views.attending'),
    url(r'^DND.html', 'info.views.dnd'),
    url(r'^contact', 'info.views.contact'),
    url(r'^events', 'info.views.events')
)
