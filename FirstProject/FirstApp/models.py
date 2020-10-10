from django.db import models,connection

class EmpManager(models.Manager):

    def getList(s):
        return s.all()

    def getselectedlist(s):
        mlist=[]
        for i in s.all():
            lk=[]
            lk.append(i.id)
            lk.append(i.name)
            lk.append(i.salary)
            mlist.append(lk)
        return mlist
    
    def get_queryset(s):
        return super().get_queryset().order_by('salary')

    def get_my_query(s):
        sql='select name,salary from firstapp_emp order by name'
        cr=connection.cursor()
        cr.execute(sql)
        el=cr.fetchall()
        return el

class Emp(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    salary=models.IntegerField()
    address=models.TextField(max_length=300)
    em=models.Manager()
    emps=EmpManager()

    def __str__(s):
        return s.name

from django import forms
class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
