from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView,CreateView,UpdateView
from .models import Prueba

# Create your views here.

from django.views.generic import TemplateView, ListView

class PruebaView(TemplateView):
    template_name='home/prueba.html'

class SuccessView(TemplateView):
    template_name='home/success.html'

   


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name='lista_nombres'
    queryset=['camilo','alex','anyi','andrea']

class ListarPruebatListView(ListView):
    template_name = "home/listarUsuarios.html"
    model=Prueba
    context_object_name='listar_usuarios'
    
class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model=Prueba
    fields=('__all__')
    success_url= '.'
    
class PruebaUpdate(UpdateView):
    template_name = "home/update.html"
    model=Prueba
    fields=('__all__')
    success_url= reverse_lazy('home_app:correcto')
  