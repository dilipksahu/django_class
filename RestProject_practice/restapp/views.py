from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializer import EmpSerializer, AccountSerializer
from .models import Emp,Account

def home(request):
    return HttpResponse("<h2>Rest API Project</h2>")

# Insert Emp Data
class CreateEmp(generics.CreateAPIView):
    serializer_class = EmpSerializer

# Display Emp Data
class EmpListView(generics.ListAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Insert and Dispaly Emp Data
class CreateEmpListView(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Display Emp Data using pk
class GetEmp(generics.RetrieveAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Update Emp data using pk with no display data
class UpdateEmp(generics.UpdateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Delete Emp data using pk with no display data
class DeleteEmp(generics.DestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Update Emp data using pk with display data
class RUpdateEmp(generics.RetrieveUpdateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Delete Emp data using pk with display data
class RDeleteEmp(generics.RetrieveDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# Display,Update and Delete Emp Data
class RUDEmp(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer



#------------------------ Account ------------------------------

# Insert Account Data
class CreateAcc(generics.CreateAPIView):
    serializer_class = AccountSerializer

# Display Account Data
class AccListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Insert and Display Account Data
class CreateAccListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Display,Update and Delete Account Data
class RUDAcc(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


#------------------ Viewsets and Routers -------------------

from rest_framework import viewsets

# ModelViewSet : Perform Insert,Display,Update and Delete operation
class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

# ---------------- Relational Models Views ------------------
from .models import Singer,Songs
from django.contrib.auth.models import User
from .serializer import UserSerializer,SingerSerializer,SongsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer