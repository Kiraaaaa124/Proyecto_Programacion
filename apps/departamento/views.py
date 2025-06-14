from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from apps.departamento.models import Departamento
from django.urls import reverse_lazy

class ListaDepartamentosView(ListView):
    model = Departamento
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        activo = self.request.GET.get('activo')

        if activo == 'true':
            return Departamento.objects.filter(activo=True)
        elif activo == 'false':
            return Departamento.objects.filter(activo=False)
        return Departamento.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activo_actual'] = self.request.GET.get('activo', '')
        return context
        

class CrearDepartamentosView(CreateView):
    model = Departamento
    fields = ['nombre','sigla','activo','piso','oficina']
    template_name = 'departamento/crear_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

class UpdateDepartamentoView(UpdateView):
    model = Departamento
    fields = ['nombre','sigla','activo','piso','oficina']
    template_name = 'departamento/editar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

class DeleteDepartamentoView(DeleteView):
    model = Departamento
    template_name = 'departamento/eliminar_departamento.html'
    success_url = reverse_lazy('lista_departamentos')

