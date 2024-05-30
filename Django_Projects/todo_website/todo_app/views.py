from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def homepage(request):
    if request.method == 'GET':
        data = Todo.objects.all()
        return render(request, 'index.html', {'data':data})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'createtask.html')
    else:
        Todo(
            title = request.POST['title'],
            description = request.POST['description']
        ).save()
        return render(request, 'createtask.html')

def check_status(request, id):
    data = Todo.objects.get(id = id)
    data.completed = True
    return redirect('home')

def delete(request, id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('home')

