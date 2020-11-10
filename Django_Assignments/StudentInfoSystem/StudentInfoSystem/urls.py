
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from student.views import UserViewSet,StudentViewSet

router = routers.DefaultRouter()
router.register(r'studs',StudentViewSet)
router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('student.urls')),
    path('',include('rest_framework.urls')),
    path('',include(router.urls)),
]
