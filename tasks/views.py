from django.shortcuts import redirect, render, get_object_or_404

from tasks.forms import TaskForm
from .models import Task

# To GET all tasks
def home(request):
  tasks = Task.objects.all().values('id', 'title', 'completed', 'created_at')
  reformed_tasks = []
  for task in tasks:
    reformed_tasks.append({
      'id': task["id"],
      'title': task['title'],
      'completed': task['completed'],
      'createdAt': task['created_at'] # Converts snake case to camel case
    })
  return render(request, 'tasks/home.html', {'tasks': reformed_tasks})

# To POST a task
def add_task(request):
  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("home")
    
  else:
      form = TaskForm()
  
  return render(request, 'tasks/add_task.html', {'form': form})

def update_task(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  task.completed = not task.completed
  task.save()
  
  return redirect('home')

def delete_task(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  task.delete()
  
  return redirect('home')