
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('reg',v.addUser),
    path('register',v.register),
    path('addEmp',v.addEmp),
    path('addStudent',v.addStudent),
    path('addAccount',v.addAccount),
    path('empList',v.getEmpList),
    path('studentList',v.getStudentList),
    path('accountList',v.getAccountList),
    path('deleteEmp',v.deleteEmp),
    path('deleteStd',v.deleteStd),
    path('deleteAcc',v.deleteAcc),
    path('editEmp',v.editEmp),
    path('editStd',v.editStd),
    path('editAcc',v.editAcc),
    
]
