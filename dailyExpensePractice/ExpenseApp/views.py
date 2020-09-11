from django.shortcuts import render
from .forms import UserForm,IncomeForm,ExpenseForm

def home(request):
    return render(request,'home.html')

# ************************ Form ************************
def addUser(request):
    f = UserForm
    return render(request,'form.html',{'form':f})

def addIncome(request):
    f = IncomeForm
    return render(request,'form.html',{'form':f})

def addExpense(request):
    f = ExpenseForm
    return render(request,'form.html',{'form':f})
