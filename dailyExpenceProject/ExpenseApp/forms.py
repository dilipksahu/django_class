from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Income,Expense

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = "__all__"

# class LoginForm(forms.Form):
#     username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
#     pwd = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))