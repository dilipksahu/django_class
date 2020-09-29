from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Product,Cart,User,PlaceOrder
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout

def index(request):
    cl = Category.objects.all()
    pl = Product.objects.all()
    d = {'cl':cl,'pl':pl}
    return render(request,'index.html',d)

def getByCategory(request,id):
    pl=Product.objects.filter(category=id)
    cl=Category.objects.all()
    d={'cl':cl,'pl':pl}
    return render(request,'index.html',d)


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
            request.session['uId'] = usr.id
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

def search(request):
    cl=Category.objects.all()

    if request.method=='POST':
        pname=request.POST.get('shr')
        pl=Product.objects.filter(pname__icontains=pname)  
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
    else:
        pl=Product.objects.all() 
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)

def edit_profile(request):
    uId = request.session.get('userId')
    user = User.objects.get(id=uId)
    cl=Category.objects.all()
    if request.method == "POST":
        f=UserForm(request.POST,instance=user)
        f.save()
        return redirect("/")
    else:
        f=UserForm(instance=user)
        d={'cl':cl,'form':f}
        return render(request,'forms.html',d)

def addToCart(request,id):
    cart=Cart()
    pd=Product.objects.get(id=id)
    print('------->',pd)
    cart.Product=pd
    uid=request.session.get('uId')
    usr=User.objects.get(id=uid)
    print('------------> ',usr)
    cart.user=usr
    cart.save()
    return redirect('/')

def getCartList(request):
    uid=request.session.get('uId')
    if request.method=='POST':
        odr=PlaceOrder()
        totalBill=request.POST.get('totalBill')
        print('--------------> ',totalBill)
        usr=User.objects.get(id=uid)
        odr.totalBill=totalBill
        odr.user=usr
        if odr is not None:
            odr.save()
            clist=Cart.objects.filter(user_id=uid)
            for i in clist:
                i.delete()
            return redirect('/')
        else:
            return HttpResponse("Error in CART List Delete Operations")
    else:
        clist=Cart.objects.filter(user_id=uid)
        cl=Category.objects.all()
        totalBill=0
        for i in clist:
            totalBill=totalBill+i.Product.price
        d={'cl':cl,'clist':clist,'totalBill':totalBill}
        return render(request,'cartList.html',d)

def deleteCart(request,id):
    cid = Cart.objects.get(id=id)
    cid.delete()
    return redirect('/Acccartlist')

def getOrderList(request,id):
    ol=PlaceOrder.objects.filter(user_id=id)
    cl=Category.objects.all()
    d={'ol':ol,'cl':cl}
    return render(request,'orderList.html',d)

# its only Image Practice
from .models import ImageData,ImageForm
def imgaccess(request):
    f=ImageForm
    if request.method=='POST':
        imgf=ImageForm(request.POST,request.FILES)
        imgf.save()
        imgList=ImageData.objects.all()
        d={'form':f,'imglist':imgList}
        return render(request,'imgAccess.html',d)
    else:
        imgList=ImageData.objects.all()
        d={'form':f,'imglist':imgList}
        return render(request,'imgAccess.html',d)
