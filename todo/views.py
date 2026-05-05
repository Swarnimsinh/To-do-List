from django.shortcuts import render
from .models import Task
from .forms import TodoForm
from django.shortcuts import get_object_or_404, redirect

def todo_list(request):
    
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        task = form.save(commit=False)
        task.save()
        return redirect('todo_list')
    else:
        form = TodoForm()
        
    tasks = Task.objects.all().order_by('-created_at')
    return render(request,'todo_list.html',{
        'form': form,
        'tasks':tasks
        })

def delete(request,id):
    tasks = get_object_or_404(Task, id=id)
    tasks.delete()
    return redirect('todo_list')

def complete(request,id):
    task = get_object_or_404(Task,id=id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('todo_list')
