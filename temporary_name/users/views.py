from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def tasks_view(request):
    return render(request, 'tasks.html')