from django.contrib import admin
from django.urls import path, include
from projects import views as project_views
from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('', project_views.index, name='home'),  # root URL izsauc index skatu
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
