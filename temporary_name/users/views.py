from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    
    return render(request, 'login.html', {'form': form})

def tasks_view(request):
    return render(request, 'tasks.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('logout.html') 
