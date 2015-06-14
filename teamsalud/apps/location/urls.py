# condig=utf-8

from django.conf.urls import patterns, url

from .views import HomeView
from .views import ResultView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^result/(?P<condicion>[A-Z0-9_-]{3})/(?P<alerta>[a-z0-9_-]+)/(?P<ubigeo>[a-z0-9_-]+)/$', ResultView.as_view(), name='result'),
)