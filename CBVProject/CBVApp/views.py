from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView


class home(TemplateView):
    template_name='index.html'
