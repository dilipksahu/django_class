from django.shortcuts import render,HttpResponse
from rest_framework import generics,viewsets
from .serializer import StudentSerializer,UserSerializer
from .models import Student
from django.contrib.auth.models import User

def home(request):
    return HttpResponse("<h3>Student Information System</h3>")


class CreateStudent(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListStudent(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUDStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

