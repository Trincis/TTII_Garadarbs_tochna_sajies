from django.urls import path, include
from django.contrib import admin
from temporary_name import views as temp_views
from tasks import views as task_views  # if you want tasks views separately
from projects import views as project_views  # if you have a projects app

urlpatterns = [
    path('', temp_views.index, name='index'),
    path('dashboard/', temp_views.dashboard, name='dashboard'),
    
    # Define or import login_view or remove this if it doesn't exist yet
    # path('login/', temp_views.login_view, name='login'),  

    path('projects/', project_views.projects, name='projects'),

    path('tasks/', temp_views.tasks, name='tasks'),
    path('tasks/update/<int:task_id>/', temp_views.update_task, name='update_task'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
