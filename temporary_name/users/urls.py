from django.urls import path
from users import views as user_views
from projects import views as project_views

urlpatterns = [
    path('', project_views.index, name='home'),
    path('projects/', project_views.projects, name='projects'),
    path('tasks/', project_views.tasks, name='tasks'),
    path('login/', user_views.login_view, name='login'),
]
