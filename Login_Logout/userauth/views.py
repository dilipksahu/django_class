from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home_page(request):
    return render(request,'home.html')  

def register_user(request):
    if request.method == 'GET':
        registerform = RegisterForm()
    else:
        registerform = RegisterForm(request.POST)
        print(request.POST)
    context = {'form':registerform}
    # Applying server side validation
    if registerform.is_valid():
        # load the data from the dictionary
        fname = registerform.cleaned_data.get('fname')
        lname = registerform.cleaned_data.get('lname')
        username = registerform.cleaned_data.get('username')
        email = registerform.cleaned_data.get('email')
        pwd = registerform.data.get('pwd')
        user = User.objects.create_user(username=username,first_name=fname,last_name=lname,password=pwd)
        if user:
            context['form'] = RegisterForm()
            context['message'] = "User has been created successfully...!"
        else:
            context['message'] = "Something want wrong please contact admin."
        
    return render(request,'userauth/register.html',context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {'form':login_form}
    if login_form.is_valid():
        un = login_form.data.get('username')
        pwd = login_form.data.get('pwd')
        # autheticate create a database query and fetch the user 
        # based on username and password
        user = authenticate(username=un,password=pwd)
        # if user is found it return an object
        # if  user is not found it return None
        if user:
            login(request,user)
            # request is sent, session is being created
            # session details are stored in the database
            return redirect('home')
        context['errmsg'] = "Invalid Credentails"
    return render(request,'userauth/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('home')



