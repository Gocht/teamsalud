from django.conf.urls import patterns, include, url
from django.contrib import admin
from teamsalud.apps.location.views import HomeTemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamsalud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/',
        HomeTemplateView.as_view(),
        name='home'),
)
