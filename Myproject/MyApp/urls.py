
from django.contrib import admin
from django.urls import path
from . import views as v
#from MyApp import views

urlpatterns = [
    path('', v.home),
    path('addUser',v.addUser),
    path('click1',v.myClick1),
    path('click2',v.myClick2),
    path('click3',v.myClick3),
    path('click4',v.myClick4),
]
