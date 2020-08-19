
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('addEmp',v.addEmp),
    path('addStudent',v.addStudent),
    path('addAccount',v.addAccount),
    
]