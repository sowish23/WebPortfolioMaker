from django.shortcuts import render ,redirect
from .models import *
from .forms import ProfileForm, ProjectForm

# def index(request):
#     return render(request, 'index.html')

def login(request):
    return render(request, 'Login.html')

def signup(request):
    return render(request, 'Signup.html')

def home(request):
    profile = Profile.objects.all()
    projects = ProjectBoard.objects.all()
    context = {'profile' : profile, 'projects': projects}
    return render(request, 'Home.html', context)

# def edit(request):
#     return render(request, 'Edit.html')

def edit(request, user_id):
    profile = Profile.objects.get(user_id = user_id)
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProfileForm(instance=profile)
        context ={
            'form' : form,
            'writing' : True,
            'now' : 'edit'
        }
    return render(request, 'Edit.html', context)

def project(request):
    if request.method=='POST':
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = ProjectForm()
    return render(request, 'Project.html', {'form': form})