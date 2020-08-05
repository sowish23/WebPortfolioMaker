from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'Login.html')

def signup(request):
    return render(request, 'Signup.html')

def home(request):
    return render(request, 'Home.html')

def edit(request):
    return render(request, 'Edit.html')
