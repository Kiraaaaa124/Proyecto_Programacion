from django.contrib import admin
from apps.empleado.models import Empleado
from datetime import date


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'departamento',
        'edad', 
    )
    
    search_fields = ('nombre', 'apellido')
    
    list_filter = ('departamento', 'trabajo')
    
    def edad(self,obj):
        today = date.today()
        age = today.year - obj.fechaNac.year - ((today.month, today.day) < (obj.fechaNac.month, obj.fechaNac.day))
        return age

admin.site.register(Empleado, EmpleadoAdmin)
