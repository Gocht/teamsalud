from django.contrib import admin
from .models import Condicion, SignoAlerta, CondicionSignoAlerta, TipoCategoria

# Register your models here.

class CondicionAdmin(admin.ModelAdmin):
    pass


class SignoAlertaAdmin(admin.ModelAdmin):
	pass


class CondicionSignoAlertaAdmin(admin.ModelAdmin):
    pass


class TipoCategoriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Condicion, CondicionAdmin)
admin.site.register(SignoAlerta, SignoAlertaAdmin)
admin.site.register(CondicionSignoAlerta, CondicionSignoAlertaAdmin)
admin.site.register(TipoCategoria, TipoCategoriaAdmin)