from django.shortcuts import render,redirect
from .models import UserFirstForm,UserF1Form,UserF1Form,UserF2Form,UserFinalForm

def home(request):
    return render(request,'index.html')

def getFirstUser(request):
    if request.method=='POST':
        f=UserFirstForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserFirstForm
        return render(request,'forms.html',{'form':f})


def getSecondUser(request):
    if request.method=='POST':
        f=UserF1Form(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserF1Form
        return render(request,'forms.html',{'form':f})


def getThirdUser(request):
    if request.method=='POST':
        f=UserF2Form(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserF2Form
        return render(request,'forms.html',{'form':f})

def getFinalUser(request):
    if request.method=='POST':
        f=UserFinalForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserFinalForm
        return render(request,'forms.html',{'form':f})

# ************************* Many To Many Relationship *****************************
from .models import Singer,SingerForm,Songs,SongForm

def addSinger(request):
    if request.method=='POST':
        f=SingerForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=SingerForm
        return render(request,'forms.html',{'form':f})

def addSongs(request):
    if request.method=='POST':
        f=SongForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=SongForm
        return render(request,'forms.html',{'form':f})

def getsglist(request):
    sgl = Songs.objects.all()
    return render(request,'sglist.html',{'sg':sgl})