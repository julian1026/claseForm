from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class Prueba2View(TemplateView):
    template_name='prueba2.html'
