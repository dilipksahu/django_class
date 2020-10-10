# ****************** Model-Manager *******************************

from django.shortcuts import render,HttpResponse,redirect

from .models import Emp,EmpForm

def addEmp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        f=EmpForm
        return render(request,'forms.html',{'form':f})
    else:
        f=EmpForm
        return render(request,'forms.html',{'form':f})

def getEmpList(request):
    el=Emp.emps.all()
    print(el)
    print('-------------------------------------')
    print('-------------------------------------')
    el1=Emp.emps.getList()
    print(el1)
    print('-------------------------------------')
    print('-------------------------------------')
    el2=Emp.emps.getselectedlist()
    print(el2)
    print('-------------------------------------')
    print('-------------------------------------')
    el3=Emp.emps.get_queryset()
    print(el3)
    print('-------------------------------------')
    print('-----------=================--------------------------')
    el=Emp.emps.all()
    print(el)
    print('-------------------------------------')
    print("++++++++++++++++++++++++++++")
    el=Emp.em.all()
    print(el)
    print('=============================')
    el5=Emp.emps.get_my_query()
    for i in el5:
        print(i)
    return HttpResponse('<h1>Check result on Console</h1>')
