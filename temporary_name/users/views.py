from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')

def tasks_view(request):
    return render(request, 'tasks.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('logout.html')  # Redirect user to login page after logout
