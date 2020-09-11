from django.shortcuts import render,redirect
from . forms import IncomeForm,ExpenseForm,UserForm
from .models import Income,Expense,User


def home(request):
    uname=request.session.get('uname')
    uId=request.session.get('userId')
    incl=Income.objects.filter(user_id=uId)
    expl=Expense.objects.filter(user_id=uId)
    totalIncome=0
    for i in incl:
        totalIncome=totalIncome+i.income
    # print("-----------------------> Total income is : ",totalIncome ) 
    totalExpense=0
    for i in expl:
        totalExpense=totalExpense+i.expense
    # print("-----------------------> Total Expense is : ",totalExpense ) 
    totalBalance=totalIncome-totalExpense
    d={'uname':uname,'bal':totalBalance}
    return render(request,'home.html',d)

def addUser(request):
    if request.method == 'POST':
        f = UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = UserForm
        return render(request,'form.html',{'form':f})

def addIncome(request):
    uname=request.session.get('uname')
    uId=request.session.get('userId')
    user=User.objects.get(username=uname)
    if request.method == 'POST':
        f = IncomeForm(request.POST,instance=user)
        f.save()
        return redirect("/")
    else:
        f = IncomeForm(instance=user)
        return render(request,'form.html',{'form':f})

def addExpense(request):
    if request.method == 'POST':
        uId=request.session.get('userId')
        incl=Income.objects.filter(user_id=uId)
        expl=Expense.objects.filter(user_id=uId)
        totalIncome=0
        for i in incl:
            totalIncome=totalIncome+i.income
        totalExpense=0
        for i in expl:
            totalExpense=totalExpense+i.expense
        totalBalance=totalIncome-totalExpense
        exp = int(request.POST.get('expense'))
        if totalBalance > exp:
            f = ExpenseForm(request.POST)
            f.save()
            return redirect("/")
        else:
            f = ExpenseForm
            expmsg = "Balance in your account is insufficient...!"
        return render(request,'form.html',{'form':f,'expmsg':expmsg})
    else:
        f = ExpenseForm
        return render(request,'form.html',{'form':f})

# ********************** Show List ******************************
def getIncomeList(request):
    uId=request.session.get('userId')
    incomelist = Income.objects.filter(user_id=uId)
    return render(request,'incomeList.html',{'incomelist':incomelist})

def getExpenseList(request):
    uId=request.session.get('userId')
    expenselist = Expense.objects.filter(user_id=uId)
    return render(request,'expenseList.html',{'expenselist':expenselist})

# ********************** Delete *******************************
def deleteIncome(request):
    inid = request.GET.get('id')
    inc = Income.objects.get(id=inid)
    inc.delete()
    return redirect('/incomeList')

def deleteExpense(request):
    exid = request.GET.get('id')
    exp = Expense.objects.get(id=exid)
    exp.delete()
    return redirect('/expenseList')

# ********************** Edit *******************************
def editIncome(request):
    inid = request.GET.get('id')
    inc = Income.objects.get(id=inid)
    if request.method == 'POST':
        f = IncomeForm(request.POST,instance=inc)
        f.save()
        return redirect('/incomeList')
    else:
        f = IncomeForm(instance=inc)
        d = {'form':f}
        return render(request,'form.html',d)

def editExpense(request):
    exid = request.GET.get('id')
    exp = Expense.objects.get(id=exid)
    if request.method == 'POST':
        f = ExpenseForm(request.POST,instance=exp)
        f.save()
        return redirect('/expenseList')
    else:
        f = ExpenseForm(instance=exp)
        d = {'form':f}
        return render(request,'form.html',d)

# *********************** Login and Logout ********************
from django.contrib.auth import authenticate,login,logout
def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            request.session['userId']=usr.id
            request.session['uname']=usr.username
            login(request,usr)
            return redirect('/')
        else:
            return render(request,'login.html',{'msglogin':"Invlaid UserName and Password"})
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")


def editProfile(request):
    uId=request.session.get('userId')
    user = User.objects.get(id=uId)
    if request.method == 'POST':
        f = UserForm(request.POST,instance=user)
        f.save()
        return redirect('/')
    else:
        f = UserForm(instance=user)
        return render(request,'form.html',{'form':f})




'''
For all User
Home,Register,Login,About us

For Login user
Home,addIcome,addExpense,IncomeList,ExpenseList,detate/edit,Feedback,contact-us,Logout
'''