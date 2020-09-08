from django.shortcuts import render,redirect
from . forms import IncomeForm,ExpenseForm,UserForm
from .models import Income,Expense,User

# Create your views here.
def home(request):
    return render(request,'home.html')

def addUser(request):
    if request.method == 'POST':
        f = UserForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = UserForm
        return render(request,'form.html',{'form':f})

def addIncome(request):
    if request.method == 'POST':
        f = IncomeForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = IncomeForm
        return render(request,'form.html',{'form':f})

def addExpense(request):
    if request.method == 'POST':
        f = ExpenseForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = ExpenseForm
        return render(request,'form.html',{'form':f})

# ********************** Show List ******************************
def getIncomeList(request):
    incomelist = Income.objects.all()
    return render(request,'incomeList.html',{'incomelist':incomelist})

def getExpenseList(request):
    expenselist = Expense.objects.all()
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






'''
For all User
Home,Register,Login,About us

For Login user
Home,addIcome,addExpense,IncomeList,ExpenseList,detate/edit,Feedback,contact-us,Logout
'''