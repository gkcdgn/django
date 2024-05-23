from django.shortcuts import render
from django.views.generic import TemplateView

class AnasayfaView(TemplateView):
    template_name ='home.html'

class HakkindaView(TemplateView):
    template_name ='hakkinda.html'
# Create your views here.
