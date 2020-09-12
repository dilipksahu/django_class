from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User

def home_page(request):
    return render(request,'home.html')

def register_user(request):
    if request.method == "GET":
        registerform = RegisterForm()
    else:
        registerform = RegisterForm(request.POST)
    context = {'form':registerform}
    # Applying server side form all fields validation
    if registerform.is_valid():
        fname = registerform.cleaned_data.get('fname')
        lname = registerform.cleaned_data.get('lname')
        email = registerform.cleaned_data.get('email')
        username = registerform.cleaned_data.get('username')
        pwd = registerform.data.get('pwd')
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,password=pwd)
        if user:
            context['form'] = RegisterForm()
            context['message'] = "User has been created successfully...!"
        else:
            context['message'] = "Something want wrong please contact admin."
    return render(request,'userauth/register.html',context)

