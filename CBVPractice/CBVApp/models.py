from django.db import models
from django import forms

class Employee(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=300)
    cname = models.CharField(max_length=50)
    class Meta():
        db_table = 'Employee'
    def __str__(self):
        return self.name

class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = "__all__"




