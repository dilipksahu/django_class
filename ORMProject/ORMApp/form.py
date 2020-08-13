from django import forms
from .models import Emp,Student,Account

class MyForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField(max_length=30)
    gender=forms.CharField(max_length=15)

class DataForm(forms.Form):
    name=forms.CharField(max_length=30,help_text="Enter Name")
    email=forms.EmailField(max_length=30,label="Enter Email")
    gender=forms.CharField(max_length=15)
    address=forms.CharField(widget=forms.Textarea)
    passw=forms.CharField(widget=forms.PasswordInput)

# take fields from models.py declare fields
class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields="__all__"

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields="__all__"




