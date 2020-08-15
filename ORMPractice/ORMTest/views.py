from django.shortcuts import render,HttpResponse
from .form import EmpForm

def home(request):
    return render(request,"index.html")

def addEmp(request):
    if request.method == "POST":
        f = EmpForm(request.POSt)
        return render(request,"index.html")
    else:
        f = EmpForm
        return render(request,"registration.html",{'form':f})
