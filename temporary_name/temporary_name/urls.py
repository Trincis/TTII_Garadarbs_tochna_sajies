from django.contrib import admin
from django.urls import path, include
from projects import views as project_views
from users import views as user_views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', project_views.index, name='home'),         # Home page
    path('projects/', project_views.projects, name='projects'),  # Projects page
    path('tasks/', project_views.tasks, name='tasks'),  # Tasks page
    path('login/', user_views.login_view, name='login'), # Login page (adjust to your login view)
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
