import requests
import json

from django.contrib.gis.geometry.regex import json_regex
from django.db import IntegrityError
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
            'id': signo.id,
            'descripcion': signo.descripcion
            })
        return data

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['condiciones'] = Condicion.objects.all()
        context['signos_alerta'] = self.get_signo_alerta()
        return context


class ApiGetSignosAlerta(View):
    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        mimetype = 'application/json'


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
        try:
            busqueda.busqueda_id = perfil.id
            busqueda.distrito = self.district_id
            busqueda.count = 1
            busqueda.save()
        except IntegrityError:
            registro = RegistroBusquedas.objects.get(busqueda=perfil.id, distrito=self.district_id)
            registro.count = registro.count +1
            registro.save()
        return True

    def get_result(self):
        data = []
        perfil = CondicionSignoAlerta.objects.get(condicion_id=self.condicion_id, signo_alerta_id=self.signo_alerta_id)
        categoria = perfil.tipo_categoria.codigo
        self.register_busqueda(perfil)
        pk=0
        results = self.get_establecimientos(categoria=categoria)
        for result in results:
            pk=pk+1
            data.append({
                'pk':pk,
                'renaes': result['cdigo_nico'],
                'institucion': result['institucin'],
                'nombre_establecimiento': result['nombre_del_establecimiento'],
                'latitud': result['norte'],
                'longitud': result['este'],
                'clasificacion': result['clasificacin'],
                'departamento': result['departamento'],
                'direccion': result['direccin'],
                'provincia': result['provincia'],
                'distrito': result['distrito'],
                'telefono': result['telfono'],
                'horario': result['horario']
            })
        return data

    def get_location(self, results):
        data = []
        for result in results:
            data.append({
                'lat':result.get('latitud'),
                'lng':result.get('longitud')
            })
        return data

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        self.condicion_id = 1
        self.signo_alerta_id = 1
        self.district_id = self.kwargs['ubigeo']
        results = self.get_result()
        context['results'] = results
        context['location'] = json.dumps(self.get_location(results))
        return context


class LogView(TemplateView):
    template_name = 'log.html'

    def get_logs(self):
        data = []
        busquedas = RegistroBusquedas.objects.all()

        for busqueda in busquedas:
            data.append({
                'condicion_id': busqueda.busqueda.condicion.id,
                'condicion': busqueda.busqueda.condicion.nombre,
                'signo__alerta_id': busqueda.busqueda.signo_alerta.id,
                'signo_alerta': busqueda.busqueda.signo_alerta.descripcion,
                'ubigeo': busqueda.distrito,
                'cantidad': busqueda.count
            })

        return data

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        context['logs'] = self.get_logs()
        return context

