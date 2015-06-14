# condig=utf-8

from django.conf.urls import patterns, url

from .views import HomeView
from .views import ResultView
from .views import LogView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^result/(?P<condicion>[0-9])/(?P<alerta>[0-9]+)/(?P<ubigeo>[0-9]+)/$', ResultView.as_view(), name='result'),
    url(r'^log/$', LogView.as_view(), name='log'),
)