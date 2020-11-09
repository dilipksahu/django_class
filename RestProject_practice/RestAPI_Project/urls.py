
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from restapp.views import EmpViewSet,UserViewSet,SingerViewSet,SongsViewSet

router = routers.DefaultRouter()
router.register(r'emps',EmpViewSet)
router.register(r'users',UserViewSet)
router.register(r'singers',SingerViewSet)
router.register(r'songs',SongsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restapp.urls')),
    path('',include('rest_framework.urls')),
    path('',include(router.urls)),
]
