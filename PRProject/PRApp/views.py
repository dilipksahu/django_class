from django.shortcuts import render, HttpResponse, redirect
from . import DBM as db

def home(request):
    return render(request,"index.html")

def addUser(request):
    return render(request,'addUser.html')

def insertData(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    salary = request.POST.get('salary')
    t=(id,name,contact,email,salary)
    db.addUser(t)
    return redirect('/userList')

def userList(request):
    ulist=db.selectAllUser()
    return render(request,"ulist.html",{"ul":ulist})

def deleteUser(request):
    id=request.GET.get('id')
    db.deleteUser(id)
    return redirect('/userList')

def editUser(request):
    id=request.GET.get('id')
    u=db.selectUserById(id)
    print('---------------->',u)
    return render(request,'updateUser.html',{'u':u})




# ORM ---> Object Relational Mapping

# Manual Operations