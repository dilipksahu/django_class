from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,FormView,CreateView,ListView,DeleteView,UpdateView
from .models import Employee,EmployeeForm

class Home(TemplateView):
    template_name = "index.html"

class FormEmp(FormView):
    template_name = 'addEmployee.html'
    form_class = EmployeeForm

class InsertEmp(CreateView):
    model = Employee
    fields = "__all__"
    success_url = "/"

class EmpList(ListView):
    model = Employee
    template_name = "empList.html"

class DeleteEmp(DeleteView):
    model = Employee
    success_url = "/empList"

class SDeleteEmp(DeleteView):
    template_name = "confirm_delete.html"
    model = Employee
    success_url = "/empList"

class EditEmp(UpdateView):
    template_name = "updateEmp.html"
    model = Employee
    fields = "__all__"
    success_url = "/empList"