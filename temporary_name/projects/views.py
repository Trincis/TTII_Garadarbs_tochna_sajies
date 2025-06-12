from django.shortcuts import render
from customlog.models import AuditLog

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def tasks(request):
    return render(request, 'tasks.html')

def update_project(request, project_id):
    # your update logic here
    
    # After update:
    AuditLog.objects.create(
        user=request.user,
        action=f"Updated project {project_id}"
    )