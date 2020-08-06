from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'index.html')

def addUser(request):
    return render(request,'addUser.html')


def myClick1(request):
    return render(request,'mypage1.html')

def myClick4(request):
    return render(request,'mypage2.html')

def myClick3(request):
    return render(request,'mypage3.html')

def myClick2(request):
    return render(request,'mypage4.html')    

def insertData(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    print("-----------------------> ",id,name,salary,contact,email)
    return render(request,'index.html') 

def addEmp(request):
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        salary=request.POST.get('salary')
        t=(id,name,salary)
        return HttpResponse("<h1>"+str(t)+"</h1>")
    
    else:
        return render(request,'addEmp.html')
