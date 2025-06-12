from django.shortcuts import render, get_object_or_404, redirect
#from customlog.models import AuditLog
from tasks.models import Task
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def tasks(request):
    return render(request, 'tasks.html')

def dashboard(request):
    return render(request, "Dashboard.html")

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        new_title = request.POST.get('title')
        if new_title:
            task.title = new_title
            task.save()

            AuditLog.objects.create(
                user=request.user,
                action=f"Updated task: {task.title}"
            )

            return redirect('tasks')  # Redirect to tasks page after update

    return render(request, 'update_task.html', {'task': task})