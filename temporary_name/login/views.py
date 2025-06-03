from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')  # Make sure the template exists
