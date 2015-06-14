from django.shortcuts import render
from django.views.generic import TemplateView, View
from models import Condicion
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['condiciones'] = Condicion.objects.all()
        return context


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['condiciones'] = Condicion.objects.all()
        return context


