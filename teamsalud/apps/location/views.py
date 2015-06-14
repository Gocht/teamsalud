import requests
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

    # Id repos
    CALLAO_ID = 'a642ff3d-23fd-451c-a4f3-e0cc81278f13'
    LIMA_ID = '859ec121-00c3-4c74-b275-5664e57b44d4'

    def get_establecimientos(self, categoria):

        url = 'http://datos.minsa.gob.pe/api/action/datastore/search.json'
        payload = {
            'resource_id': self.CALLAO_ID,
        }

        response = requests.get(url, params=payload)
        response = response.json()

        def _filter(renaes):
            return [renae for renae in renaes if renae['ubigeo'] == self.kwargs['ubigeo'] and renae['categoria'] == categoria]

        if response.get('success', False):
            _list = response.get('result', {}).get('records', [])
            establecimientos = _filter(renaes=_list)
        else:
            establecimientos = []

        return establecimientos

    def register_busqueda(self, perfil):
        busqueda = RegistroBusquedas()
        busqueda.busqueda = perfil
        busqueda.distrito = self.district_id
        busqueda.save()

    def get_result(self):
        result = []
        # perfil = CondicionSignoAlerta.objects.get(condicion_id=self.condicion_id, signo_alerta_id=self.signo_alerta_id)
        perfil = None
        # categoria_id = perfil.tipo_categoria_id
        # self.register_busqueda(perfil)

        results = self.get_establecimientos(categoria='I-4')

        for result in results:
            result.append({
                'renaes': result['cdico_nico'],
                'institucion': result['institucin'],
                'nombre_establecimiento': result['nombre_del_establecimiento'],
                'latitud': rresult['norte'],
                'longitud': result['este'],
                'clasificacion': result['clasificacin'],
                'departamento': result['departamento'],
                'direccion': result['direccin'],
                'provincia': result['provincia'],
                'distrito': result['distrito'],
                'telefono': result['telfono'],
                'horario': result['horario']
            })
        return result

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        self.condicion_id = 1
        self.signo_alerta_id = 1
        self.district_id = 1501
        context['results'] = self.get_result()
        return context

