from django.contrib import admin
from .models import Condicion, SignoAlerta

# Register your models here.

class CondicionAdmin(admin.ModelAdmin):
    pass


class SignoAlertaAdmin(admin.ModelAdmin):
	pass


admin.site.register(Condicion, CondicionAdmin)
admin.site.register(SignoAlerta, SignoAlertaAdmin)