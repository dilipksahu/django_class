from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserFirstForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class UserF1(models.Model):
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class UserF2(models.Model):
    contact=models.IntegerField()
    middleName=models.CharField(max_length=10)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class UserF1Form(forms.ModelForm):
    class Meta:
        model=UserF1
        fields='__all__'

class UserF2Form(forms.ModelForm):
    class Meta:
        model=UserF2
        fields='__all__'

# Inherit from auth.User 
class UserFinal(User):
    age=models.IntegerField()
    contact=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)

class UserFinalForm(UserCreationForm):
    class Meta:
        model=UserFinal
        fields=['username','first_name','middle_name','last_name','email','age','gender','contact','password1','password2']

# ************** Many To Many ORM Relationship *********************
class Singer(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)

    def __str__(s):
        return s.name

class SingerForm(forms.ModelForm):
    class Meta:
        model=Singer
        fields='__all__'

class Songs(models.Model):
    name=models.CharField(max_length=30)
    duration=models.IntegerField()
    sg=models.ManyToManyField(Singer)

    # function call from sglist.html 
    def getSingerName(self):
        return ','.join( str(i) for i in self.sg.all())


class SongForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields='__all__'
