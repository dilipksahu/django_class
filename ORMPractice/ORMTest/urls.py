
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('addEmp',v.addEmp),
    path('addStudent',v.addStudent),
    path('addAccount',v.addAccount),
    path('empList',v.getEmpList),
    path('stdList',v.getStdList),
    path('accList',v.getAccList),
    path('deleteEmp',v.deleteEmp),
    path('deleteStd',v.deleteStd),
    path('deleteAcc',v.deleteAcc),
    path('editEmp',v.editEmp),
    
]
