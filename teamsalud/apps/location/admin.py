from django.contrib import admin
from .models import Condicion

# Register your models here.

class CondicionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Condicion, CondicionAdmin)