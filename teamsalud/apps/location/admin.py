from django.contrib import admin
from .models import Condicion, SignoAlerta, CondicionSignoAlerta, TipoCategoria, RegistroBusquedas

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


admin.site.register(Condicion, CondicionAdmin)
admin.site.register(SignoAlerta, SignoAlertaAdmin)
admin.site.register(CondicionSignoAlerta, CondicionSignoAlertaAdmin)
admin.site.register(TipoCategoria, TipoCategoriaAdmin)
admin.site.register(RegistroBusquedas, RegistroBusquedasAdmin)