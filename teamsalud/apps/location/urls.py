# condig=utf-8

from django.conf.urls import patterns, url

from .views import HomeView
from .views import ResultView

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^result', ResultView.as_view(), name='result'),
)