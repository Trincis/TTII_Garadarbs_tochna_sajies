from django.urls import path, include
from users import views as user_views
from projects import views as project_views

urlpatterns = [
    path('projects/', project_views.projects, name='projects'),
    path('projects/new', project_views.new_project, name='new_project'),
    path('tasks/', user_views.tasks_view, name='tasks'),
    path('', project_views.login_view, name='login'),
    path('login/', project_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('tasks/', include('tasks.urls')),
    path('dashboard/', user_views.dashboard_view, name='dashboard'),
]
