
from django.contrib import admin
from django.urls import path
from . import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('',v.Home.as_view()),
    path('click',TemplateView.as_view(template_name="data.html")),
    path('formEmp',v.FormEmp.as_view()),
    path('insertEmp',v.InsertEmp.as_view()),
    path('empList',v.EmpList.as_view()),
    path('deleteEmp/<int:pk>',v.DeleteEmp.as_view()),
    path('sdeleteEmp/<int:pk>',v.SDeleteEmp.as_view()),
    path('editEmp/<int:pk>',v.EditEmp.as_view()),
]
