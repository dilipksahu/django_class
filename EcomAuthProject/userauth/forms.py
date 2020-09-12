from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    fname = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    lname = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username '}))
    pwd = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),min_length=8)
    cpwd = forms.CharField(label="",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),min_length=8)
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))

    # Server side  password validation
    def clean(self):
        data = self.data
        if data.get('pwd') != data.get('cpwd'):
            raise ValidationError("Confirm Password must be same as Password")
        return data

    # Server side username validation
    def clean_username(self):
        un = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=un).exists():
            raise ValidationError("User already exist")
        return un

class LoginForm(forms.Form):
    username =  forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Username"}))
    pwd = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))