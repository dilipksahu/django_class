from django.shortcuts import render,HttpResponse

def index(request):
    a = '''<h1>
    Welcome To My Home...
    <h3><a href="home">First Link</a></h3>
    <h3><a href="getname">Second Link</a></h3>
    </h1>'''
    return HttpResponse(a)

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def getValues(request):
    a = '''<h1>
    Welcome To Django World...
    </h1>'''
    return HttpResponse(a)


