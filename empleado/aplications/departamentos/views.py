from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class Prueba1View(TemplateView):
    template_name='prueba1.html'

    