from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,FormView,CreateView,ListView,DeleteView,UpdateView
from . models import Teacher,TeacherForm,Student,StudentForm


class home(TemplateView):
    template_name='index.html'

class AddTeacher(FormView):
    template_name= 'addTeacher.html'
    form_class= TeacherForm

class InsertTeacher(CreateView):
    model=Teacher
    fields='__all__'
    success_url="/"

class AddStudent(FormView):
    template_name= 'addStudent.html'
    form_class= StudentForm

class InsertStudent(CreateView):
    model=Student
    fields='__all__'
    success_url="/"

class TeacherList(ListView):
    model=Teacher
    template_name="teacherList.html"

class StudentList(ListView):
    model=Student
    template_name="studentList.html"

# Two method used for delete confirm in CBV - Django Structure base and template base
class DeleteTeacher(DeleteView):
    model=Teacher
    success_url="/teacherList"

class SDeleteTeacher(DeleteView):
    template_name= "teacher_confirm_delete_Op.html"
    model=Teacher
    success_url="/teacherList"

class DeleteStudent(DeleteView):
    model=Student
    success_url="/StudentList"

class SDeleteStudent(DeleteView):
    template_name= "student_confirm_delete_Op.html"
    model=Student
    success_url="/studentList"

# ********* Edit **********************
class UpdateTeacher(UpdateView):
    template_name= "updateTeacher.html"
    model=Teacher
    fields='__all__'
    success_url="/teacherList"

class UpdateStudent(UpdateView):
    template_name= "updateTeacher.html"
    model=Student
    fields='__all__'
    success_url="/studentList"



