from django.urls import path, include
from django.contrib import admin
from temporary_name import views as temp_views
from django.conf.urls.i18n import i18n_patterns  # language support
from projects import views as project_views

urlpatterns = i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),#language
    path('', project_views.login_view, name='login'),

    path('dashboard/', temp_views.dashboard, name='dashboard'),

    path('projects/', include('projects.urls')),
    path('tasks/', temp_views.tasks, name='tasks'),
    path('tasks/update/<int:task_id>/', temp_views.update_task, name='update_task'),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),

    prefix_default_language=False,  # must be last
)
