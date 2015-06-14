from django.contrib import admin
from .models import Condicion, SignoAlerta, CondicionSignoAlerta, TipoCategoria, RegistroBusquedas
from .models import RenaesServicios, RenaesEspecialidades, Servicios, Especialidades

# Register your models here.

class CondicionAdmin(admin.ModelAdmin):
    pass


class SignoAlertaAdmin(admin.ModelAdmin):
	pass


class CondicionSignoAlertaAdmin(admin.ModelAdmin):
    pass


class TipoCategoriaAdmin(admin.ModelAdmin):
    pass

class RegistroBusquedasAdmin(admin.ModelAdmin):
    pass

class EspecialidadesAdmin(admin.ModelAdmin):
    pass

class ServiciosAdmin(admin.ModelAdmin):
    pass

class RenaesServiciosAdmin(admin.ModelAdmin):
    pass

class RenaesEspecialidadesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Condicion, CondicionAdmin)
admin.site.register(SignoAlerta, SignoAlertaAdmin)
admin.site.register(CondicionSignoAlerta, CondicionSignoAlertaAdmin)
admin.site.register(TipoCategoria, TipoCategoriaAdmin)
admin.site.register(RegistroBusquedas, RegistroBusquedasAdmin)
admin.site.register(RenaesServicios, RenaesServiciosAdmin)
admin.site.register(RenaesEspecialidades, RenaesEspecialidadesAdmin)
admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)

