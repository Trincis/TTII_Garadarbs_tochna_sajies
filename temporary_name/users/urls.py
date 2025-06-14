from django.urls import path, include
from users import views as user_views
from projects import views as project_views

urlpatterns = [
    path('', user_views.index, name='home'),
    path('projects/', project_views.projects, name='projects'),
    path('projects/new', project_views.new_project, name='new_project'),
    path('tasks/', user_views.tasks_view, name='tasks'),
    path('login/', user_views.login_view, name='login'),
    path('tasks/', include('tasks.urls')),
]
