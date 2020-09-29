from django.shortcuts import render,HttpResponse
from rest_framework import generics
from .serializer import EmpSerializer,AccountSerializer
from .models import Emp,Account

def home(request):
    return HttpResponse("<h1>Welcome To Django RestProject</h1>")

# Insert Data
class CreateEmp(generics.CreateAPIView):
    serializer_class=EmpSerializer

# Display Data
class EmpListView(generics.ListAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

# Insert and Display
class CreateEmpListView(generics.ListCreateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class GetEmp(generics.RetrieveAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class UpdateEmp(generics.UpdateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class DeleteEmp(generics.DestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer


class RUpdateEmp(generics.RetrieveUpdateAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer

class RDeleteEmp(generics.RetrieveDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer


class RUDEmp(generics.RetrieveUpdateDestroyAPIView):
    queryset=Emp.objects.all()
    serializer_class=EmpSerializer


# *************** Account *************************
# Insert Data
class CreateAccount(generics.CreateAPIView):
    serializer_class=AccountSerializer

# Display Data
class AccountListView(generics.ListAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer

class CreateAccountListView(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer



