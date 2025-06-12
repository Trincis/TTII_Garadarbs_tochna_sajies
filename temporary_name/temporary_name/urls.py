from django.urls import path
from temporary_name import views as temp_views  # Import views from temporary_name app

urlpatterns = [
    path('', temp_views.index, name='index'),
    path('dashboard/', temp_views.dashboard, name='dashboard'),
    path('login/', temp_views.login_view, name='login'),
    path('projects/', project_views.projects, name='projects'),

    # Existing commented out tasks line can be replaced with:
    path('tasks/', temp_views.tasks, name='tasks'),
    path('tasks/update/<int:task_id>/', temp_views.update_task, name='update_task'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
