from django.urls import path, include
from django.contrib import admin
from temporary_name import views as temp_views

urlpatterns = [
    path('', temp_views.index, name='index'),
    path('dashboard/', temp_views.dashboard, name='dashboard'),

    path('projects/', include('projects.urls')),  # include projects.urls here

    path('tasks/', temp_views.tasks, name='tasks'),
    path('tasks/update/<int:task_id>/', temp_views.update_task, name='update_task'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
