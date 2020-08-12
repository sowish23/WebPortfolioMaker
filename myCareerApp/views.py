from django.shortcuts import render ,redirect
from .models import *
from .forms import ProfileForm, ProjectForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'Login.html')

def signup(request):
    return render(request, 'Signup.html')

def home(request):
    return render(request, 'Home.html')

# def edit(request):
#     return render(request, 'Edit.html')

def edit(request):
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm()
    return render(request, 'Edit.html', {'form': form})

def project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProjectForm()
    return render(request, 'Project.html', {'form': form})