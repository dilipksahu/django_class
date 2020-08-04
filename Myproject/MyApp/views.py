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