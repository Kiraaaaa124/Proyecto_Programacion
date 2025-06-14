from django.contrib import admin
from apps.departamento.models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_filter = ('activo',)
admin.site.register (Departamento)
