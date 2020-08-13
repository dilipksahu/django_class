from django.shortcuts import render,HttpResponse
from .form import MyForm,DataForm,EmpForm,StudentForm,AccountForm

def home(request):
    return render(request,'index.html')

def addUser(request):
    f=MyForm
    return render(request,'register.html',{'form':f})

def register(request):
    f=DataForm
    return render(request,'register.html',{'form':f})

def addEmp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return render(request,'index.html')
    else:
        f=EmpForm
        return render(request,'register.html',{'form':f})

def addStudent(request):
    if request.method=="POST":
        f=StudentForm(request.POST)
        f.save()
        return render(request,'index.html')
    else:
        f=StudentForm
        return render(request,'register.html',{'form':f})

def addAccount(request):
    if request.method=="POST":
        f=AccountForm(request.POST)
        f.save()
        return render(request,"index.html")
    else:
        f=AccountForm
        return render(request,"register.html",{'form':f})
