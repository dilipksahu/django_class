from django.contrib import admin
from django.urls import path
from . import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('',v.home.as_view()),
    path('click',TemplateView.as_view(template_name='data.html')),

]

