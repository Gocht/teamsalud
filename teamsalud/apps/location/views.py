import requests
import json

from bs4 import BeautifulSoup as bs

from django.http import HttpResponse
from django.contrib.gis.geometry.regex import json_regex
from django.db import IntegrityError
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View, RedirectView
from models import Condicion, CondicionSignoAlerta, SignoAlerta, TipoCategoria, RegistroBusquedas, RenaesServicios
from models import RenaesEspecialidades, Servicios, Especialidades
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


class Intermediate(View):


    def get(self, request, *args, **kwargs):
        condicion = 1
        signo = self.request.GET.get('signo', '')
        ubigeo = self.get_ubigeo()

        _dict = {'condicion':condicion, 'alerta': signo, 'ubigeo': ubigeo}
        return HttpResponse(json.dumps(_dict), content_type='application/json')

    def get_google_data(self):
        url = 'http://maps.googleapis.com/maps/api/geocode/json'
        payload = {
            'latlng': '%s,%s' % (self.request.GET.get('latitude', ''), self.request.GET.get('longitude', '')),
            'sensor': False
        }

        response = requests.get(url, params=payload)
        response = response.json()

        if response.get('status', '') == 'OK':
            distrito_name = response.get('results')[0].get('address_components')[2].get('long_name')
        else:
            distrito_name = ''

        return distrito_name

    def get_ubigeo(self):
        distrito_name = self.get_google_data()

        # ubigeo = '150101'

        url = 'http://webinei.inei.gob.pe:8080/sisconcode/ubigeo/listaBusquedaUbigeoPorDescripcion.htm'

        payload = {
            'versionCategoriaPK': '4-1',
            'nivel': 4,
            'descripcion': distrito_name,
            'strVersion': 2015
        }

        response = requests.get(url, params=payload)

        if response.status_code == 200:
            soup = bs(response.content)
            ubigeo = soup.find('body').find_all('table')[1].find_all('tr')[0].find_all('td')[3].text.split(' ')[0].strip()
        else:
            ubigeo = ''

        return ubigeo


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
            return [renae for renae in renaes if renae['ubigeo'] == self.kwargs['ubigeo'] and renae['categoria'] == categoria ]

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

    def get_servicios(self, renaes):
        data=[]
        servicios = RenaesServicios.objects.filter(codigo_renaes=renaes)
        for servicio in servicios:
            data.append({
                'codigo_servicio': servicio.servicio.codigo,
                'servicio': servicio.servicio.descripcion
            })
        return data

    def get_especialidades(self, renaes):
        data = []
        especialidades = RenaesEspecialidades.objects.filter(codigo_renaes=renaes)
        for especialidad in especialidades:
            data.append({
                'codigo_especialidad': especialidad.especialidad.codigo,
                'especialidad': especialidad.especialidad.descripcion
            })
        return data

    def get_result(self):
        data = []
        perfil = CondicionSignoAlerta.objects.get(condicion_id=self.condicion_id, signo_alerta_id=self.signo_alerta_id)
        categoria = perfil.tipo_categoria.codigo
        self.register_busqueda(perfil)
        pk=0
        results = self.get_establecimientos(categoria=categoria)
        for result in results:
            pk=pk+1
            renaes = result['cdigo_nico']
            data.append({
                'pk':pk,
                'renaes': renaes,
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
                'horario': result['horario'],
                'servicios': self.get_servicios(renaes),
                'especialidades': self.get_especialidades(renaes)
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


class LogApiView(View):

    def get(self, request, *args, **kwargs):
        json_data = json.dumps(self.get_logs())
        return HttpResponse(json_data, content_type='application/json')

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
