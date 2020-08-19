from django.contrib import admin
from django.urls import path
from . import views as v
from django.views.generic import TemplateView

urlpatterns = [
    path('',v.home.as_view()),
    path('click',TemplateView.as_view(template_name='data.html')),
    path('addTeacher',v.AddTeacher.as_view()),
    path('insertTeacher',v.InsertTeacher.as_view()),
    path('addStudent',v.AddStudent.as_view()),
    path('insertStudent',v.InsertStudent.as_view()),
    path('teacherList',v.TeacherList.as_view()),
    path('studentList',v.StudentList.as_view()),
    path('deleteTeacher/<int:pk>',v.DeleteTeacher.as_view()),
    path('deleteStudent/<int:pk>',v.DeleteStudent.as_view()),
    path('sdeleteTeacher/<int:pk>',v.SDeleteTeacher.as_view()),
    path('sdeleteStudent/<int:pk>',v.SDeleteStudent.as_view()),
    path('editTeacher/<int:pk>',v.UpdateTeacher.as_view()),
    path('editStudent/<int:pk>',v.UpdateStudent.as_view()),

]

