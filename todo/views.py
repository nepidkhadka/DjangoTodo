from django.shortcuts import get_object_or_404, render, redirect
from .models import Todo

# Create your views here.

def home (request):
    todos = Todo.objects.order_by("-id")
    return render(request, "todo/home.html", {"todos" : todos})

def addtodo (request):
    if request.method == "POST" :
        title = request.POST.get('title')
        des = request.POST.get('des')
        Todo.objects.create(title=title, des = des)
    
    return redirect('home')

def setdone(request, id): 
    todo = Todo.objects.get(id = id)
    todo.isDone = not todo.isDone
    todo.save()
    return redirect("home")

def delete(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect("home")

def viewupdate(request, id):
    todo = Todo.objects.get(id = id)
    return render(request, "todo/updatetodo.html", {"todo":todo})

def update(request, id):
    todo = get_object_or_404(Todo, id=id) 
    
    if request.method == "POST" :
        title = request.POST.get('title')
        des = request.POST.get('des')
        todo.title = title
        todo.des = des
        todo.save()
    
    return redirect('home')