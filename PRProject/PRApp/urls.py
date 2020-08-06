from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('addUser',v.addUser),
    path('insertData',v.insertData),
    path('userList',v.userList),
    #path('deleteUser/<int:id>',v.deleteUser),
    path('deleteUser',v.deleteUser),
    path('editUser',v.editUser),
    
]
