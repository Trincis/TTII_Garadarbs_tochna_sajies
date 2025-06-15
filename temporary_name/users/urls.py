from django.urls import path, include
from users import views as user_views
from projects import views as project_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('projects/', project_views.projects, name='projects'),
    path('projects/new', project_views.new_project, name='new_project'),
    path('tasks/', user_views.tasks_view, name='tasks'),
    path('', project_views.login_view, name='login'),
    path('login/', project_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('tasks/', include('tasks.urls')),
    path('dashboard/', user_views.dashboard_view, name='dashboard'),
]
