
from django.contrib import admin
from django.urls import path
from FirstApp import views,myviews as mv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home', views.home),
    path('getname',views.getValues),

    path('byemp',mv.addEmp),
    path('el',mv.getEmpList),
]
