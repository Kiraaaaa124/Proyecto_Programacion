from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from apps.empleado.models import Empleado 
from apps.departamento.models import Departamento

class IndexView(TemplateView):
    template_name = 'empleados/home.html'

class ListaEmpleadoView(ListView):
    model = Empleado
    template_name = 'empleados/lista_empleados.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        apellido = self.request.GET.get('apellido')
        departamento= self.request.GET.get('departamento')
        trabajo= self.request.GET.get('Trabajo')
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if departamento:
            queryset= queryset.filter(departamento__id=departamento)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_empleados'] = self.get_queryset()  # Asegura que se pasa correctamente
        context['departamentos']= Departamento.objects.all()
        return context
        
class CrearEmpleadoView(CreateView):
    model = Empleado
    fields = ['nombre','apellido','email','fecha_nac','pais','trabajo','departamento','observacion']
    template_name = 'empleados/crear_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class UpdateEmpleadoView(UpdateView):
    model = Empleado
    fields = ['nombre','apellido','email','fecha_nac','pais','trabajo','departamento','observacion']
    template_name = 'empleados/editar_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class DeleteEmpleadoView(DeleteView):
    model = Empleado
    template_name = 'empleados/eliminar_empleado.html'
    success_url = reverse_lazy('lista_empleados')

class DetailEmpleadoView(DetailView):
    model = Empleado
    template_name = 'empleados/detalle_empleado.html'


