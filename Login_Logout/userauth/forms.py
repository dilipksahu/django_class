from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    fname = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    lname = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    pwd = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    cpwd = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    # Server side Validation for password
    def clean(self):
        data = self.data # self.cleaned_data
        if data.get('pwd') != data.get('cpwd'):
            raise ValidationError("Password should be Same")
        return data

    # Username already exists
    def clean_username(self):
        un = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=un).exists():
            raise ValidationError("Username already in use")
        return un

class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    pwd = forms.CharField(label="",min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))