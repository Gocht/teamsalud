import json
from django.contrib.gis.geometry.regex import json_regex
from django.shortcuts import render
from django.views.generic import TemplateView, View
from models import Condicion, CondicionSignoAlerta, SignoAlerta, TipoCategoria, RegistroBusquedas
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_signo_alerta(self):
        data = []
        signos = SignoAlerta.objects.all()

        for signo in signos:
            data.append({
            'descripcion': signo.descripcion
            })
        return data

    def get_signo_alerta2(self):
        data = ['s','sbvhjdsbvdjhv', 'sbvhjdvdsvdv']
        return data

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['condiciones'] = Condicion.objects.all()
        context['signos_alerta'] = json.dumps(self.get_signo_alerta())
        return context


class ResultView(TemplateView):
    template_name = 'result.html'

    def get_establecimientos(self):
        establecimientos = []
        establecimientos = abc
        return establecimientos

    def register_busqueda(self, perfil):
        busqueda = RegistroBusquedas()
        busqueda.busqueda = perfil
        busqueda.distrito = self.district_id
        busqueda.save()

    def get_result(self):
        result = []
        perfil = CondicionSignoAlerta.objects.get(condicion_id=self.condicion_id, signo_alerta_id=self.signo_alerta_id)
        categoria_id = perfil.tipo_categoria_id
        self.register_busqueda(perfil)

        establecimientos = self.get_establecimientos()
        results = establecimientos.objects.filter(categoria=categoria_id, ubigeo=self.district_id)

        for result in results:
            result.append({
                'renaes': result.codigo_unico,
                'institucion': result.institucion,
                'nombre_establecimiento': result.nombre,
                'latitud': result.latitud,
                'longitud': result.longitud,
                'clasificaxion': result.clasificacion,
                'departamento': result.departamento,
                'direccion': result.direccion,
                'provincia': result.provincia,
                'distrito': result.distrito,
                'telefono': result.telefono,
                'horario': result.horario
            })
        return result

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        self.condicion_id = 1
        self.signo_alerta_id = 1
        self.district_id = 1501
        context['results'] = self.get_result()
        return context

