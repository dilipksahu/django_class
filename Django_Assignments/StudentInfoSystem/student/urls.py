

from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('addstud/',v.CreateStudent.as_view()),
    path('liststud/',v.ListStudent.as_view()),
    path('rudstud/<int:pk>/',v.RUDStudent.as_view()),
]
