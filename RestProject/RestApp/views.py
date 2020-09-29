from django.shortcuts import render,HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome To Django Restfull API</h1>")
