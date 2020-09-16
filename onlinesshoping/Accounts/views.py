from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Product,Cart,User
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout

def index(request):
    cl = Category.objects.all()
    pl = Product.objects.all()
    d = {'cl':cl,'pl':pl}
    return render(request,'index.html',d)

def getByCategory(request):
    return HttpResponse("<h1>Success</h1>")

def addUser(request):
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserForm
        pl=Product.objects.all()  # not neccessary
        cl=Category.objects.all()
        d={'cl':cl,'pl':pl,'form':f}
        return render(request,'forms.html',d)



def login_view(request):
    if request.method=='POST':
        uname = request.POST.get("uname")
        passw = request.POST.get("passw")
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            login(request,usr)
            return redirect('/')
        else:
            return render(request,'login.html',{'msglogin':"Invlaid UserName and Password"})
    else:
        pl=Product.objects.all()  
        cl=Category.objects.all()
        d={'cl':cl}
        return render(request,'login.html',d)

def logout_view(request):
    logout(request)
    return redirect("/")