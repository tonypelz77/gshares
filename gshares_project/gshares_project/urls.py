from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gshares_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'gshares_project.views.index', name='index'),
	url(r'^gshares/', include('gshares.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
