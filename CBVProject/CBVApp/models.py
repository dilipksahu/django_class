from django.db import models
from django import forms


class Teacher(models.Model):
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    college=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    Address=models.CharField(max_length=300)

    class Meta():
        db_table='Teacher'
    
    def __str__(s):
        return s.name


class TeacherForm(forms.ModelForm):
    class Meta():
        model=Teacher
        fields='__all__'



class Student(models.Model):
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    college=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    Address=models.CharField(max_length=300)

    class Meta():
        db_table='Student'

    def __str__(s):
        return s.name

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'