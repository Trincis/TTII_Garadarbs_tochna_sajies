from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Task

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

def new_project(request):
    return render(request, 'new_project.html', {'projects': projects})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def new_project(request):
    if request.method == 'POST':
        name = request.POST.get('project_name')
        description = request.POST.get('project_description')
        task_descriptions = request.POST.getlist('tasks')

        project = Project.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )

        for task_desc in task_descriptions:
            Task.objects.create(
                title=task_desc,
                description='',
                status='pending',
                project=project
            )

        return redirect('project_list')

    return render(request, 'projects/new_project.html')
