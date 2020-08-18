from django import forms
from .models import Emp,Student,Account

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"