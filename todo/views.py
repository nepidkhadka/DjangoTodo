from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def home (request):
    todos = Todo.objects.all()
    return render(request, "todo/home.html", {"todos" : todos})

def addtodo (request):
    if request.method == "POST" :
        title = request.POST.get('title')
        des = request.POST.get('des')
        Todo.objects.create(title=title, des = des)
    
    return redirect('home')