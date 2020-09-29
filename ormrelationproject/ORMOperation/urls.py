"""ormrelationproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('adduserfirst', v.getFirstUser,name='fuser'),
    path('addusersecond', v.getSecondUser,name='suser'),
    path('adduserthird', v.getThirdUser,name='tuser'),
    path('adduserfinal', v.getFinalUser,name='finaluser'),
    path('addsinger', v.addSinger,name='addsinger'),
    path('addsong', v.addSongs,name='addsong'),
    path('sglist', v.getsglist,name='addsglist'),
]