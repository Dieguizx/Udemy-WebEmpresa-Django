from django.shortcuts import render, HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("<h1>Home</h1>")

def about (reques):
    return HttpResponse("<h1>About</h1>")

def services (request):
    return HttpResponse("<h1>Services</h1>")

def store (reques):
    return HttpResponse("<h1>Store</h1>")

def contact (request):
    return HttpResponse("<h1>Contact</h1>")

def blog(request):
    return HttpResponse("<h1>Blog</h1>")

def sample(reques):
    return HttpResponse("<h1>Sample</h1>")


