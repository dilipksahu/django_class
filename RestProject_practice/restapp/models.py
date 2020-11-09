from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    address = models.TextField(max_length=300)

    def __str__(s):
        return s.name

class Account(models.Model):
    salary = models.IntegerField()
    month = models.CharField(max_length=30)
    year = models.IntegerField()
    emp = models.ForeignKey(Emp,on_delete=models.CASCADE)

#------------------- Relationship Models -----------------------

class Singer(models.Model):
    name = models.CharField(max_length=30)  
    age = models.IntegerField()
    created_user = models.ForeignKey('auth.User',related_name='singer',on_delete=models.CASCADE)

    def __str__(s):
        return s.name

class Songs(models.Model):
    title = models.CharField(max_length=30)
    duration = models.IntegerField()
    singer = models.ManyToManyField(Singer)
    created_user = models.ForeignKey('auth.User',related_name='songs',on_delete=models.CASCADE)

    def __str__(s):
        return s.title

