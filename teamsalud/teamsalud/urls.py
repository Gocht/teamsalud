from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.location import urls as location_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamsalud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(location_urls)),
)
