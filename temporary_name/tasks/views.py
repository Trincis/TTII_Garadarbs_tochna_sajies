from django.shortcuts import render
from .models import Task

def tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': all_tasks})
