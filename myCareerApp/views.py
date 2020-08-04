from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')
