from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    age = models.IntegerField()
    comname = models.CharField(max_length=15,default='')
    empaddress = models.CharField(max_length=200,default='')
    class Meta:
        db_table = "Emp"
    def __str__(s):
        return s.name
    
    
class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    stream = models.CharField(max_length=20)
    college = models.CharField(max_length=20)
    class Meta:
        db_table = "Student"
    def __str__(s):
        return s.name

class Account(models.Model):
    salary = models.IntegerField()
    month = models.CharField(max_length=15)
    emp = models.ForeignKey(Emp,on_delete=models.CASCADE)
    std = models.ForeignKey(Student,on_delete=models.CASCADE)
    class Meta:
        db_table = "Account"
    


