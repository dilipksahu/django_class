from django.shortcuts import render,HttpResponse
from .form import EmpForm,StudentForm,AccountForm


def home(request):
    return render(request,"index.html")

def addEmp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return render(request,'index.html')
    else:
        f=EmpForm
        return render(request,'registration.html',{'form':f})

def addStudent(request):
    if request.method=="POST":
        f=StudentForm(request.POST)
        f.save()
        return render(request,'index.html')
    else:
        f=StudentForm
        return render(request,'registration.html',{'form':f})

def addAccount(request):
    if request.method=="POST":
        f=AccountForm(request.POST)
        f.save()
        return render(request,'index.html')
    else:
        f=AccountForm
        return render(request,'registration.html',{'form':f})