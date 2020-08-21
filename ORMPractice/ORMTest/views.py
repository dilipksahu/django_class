from django.shortcuts import render,HttpResponse,redirect
from .form import EmpForm,StudentForm,AccountForm

# ********************************* Django Function Based Structure Modelling ************************************

def home(request):
    return render(request,"index.html")

# ********************** Models Created and Insert Data ********************
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

# ************************** Display information **************************
from .models import Emp,Student,Account

def getEmpList(request):
    emplist = Emp.objects.all()
    return render(request,'empList.html',{'emplist':emplist})

def getStdList(request):
    stdlist = Student.objects.all()
    return render(request,'studentList.html',{'stdlist':stdlist})

def getAccList(request):
    acclist = Account.objects.all()
    return render(request,'accountList.html',{'acclist':acclist})

# **************************** Delete Operarion *******************************

def deleteEmp(request):
    eid = request.GET.get('eid')
    emp = Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/empList')

def deleteStd(request):
    rno = request.GET.get('rno')
    std = Student.objects.get(roll_no=rno)
    std.delete()
    return redirect('/stdList')     # path in urls

def deleteAcc(request):
    aid = request.GET.get('aid')
    acc = Account.objects.get(id=aid)
    acc.delete()
    return redirect('/accList')
    

# ************************** Edit Operation *********************************

def editEmp(request):
    eid = request.GET.get('eid')
    emp = Emp.objects.get(id=eid)
    if request.method == 'POST':
        f = EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/empList')
    else:
        f = EmpForm(instance=emp)
        d = {'form':f}
        return render(request,'registration.html',d)

def editStd(request):
    rno = request.GET.get('rno')
    std = Student.objects.get(roll_no=rno)
    if request.method == "POST":
        f = StudentForm(request.POST,instance=std)
        f.save()
        return redirect("/stdList")
    else:
        f = StudentForm(instance=std)
        d = {'form':f}
        return render(request,"registration.html",d)

def editAcc(request):
    aid = request.GET.get('aid')
    acc = Account.objects.get(id=aid)
    if request.method == "POST":
        f = AccountForm(request.POST,instance=acc)
        f.save()
        return redirect("/accList")
    else:
        f = AccountForm(instance=acc)
        d = {'form':f}
        return render(request,"registration.html",d)