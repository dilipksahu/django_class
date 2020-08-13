from django.db import models


class Emp(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
    email=models.EmailField(max_length=30)
    myaddress=models.CharField(max_length=200,default='')
    age=models.IntegerField()
    cname=models.CharField(max_length=30,default="")
    class Meta:
        db_table='Emp'
    


class Student(models.Model):
    rollNo=models.IntegerField(primary_key=True,name="Rank")
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    college=models.CharField(max_length=30,default="")
    class Meta:
        db_table='student'



class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE,name="Emp_Id")
    std=models.ForeignKey(Student,on_delete=models.CASCADE,name="Student_Rank")
  

# makemigrations
# Migrate
# python manage.py migrate appname --zero : To reverse the migriation
