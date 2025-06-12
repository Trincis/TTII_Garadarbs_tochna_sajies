from django.urls import path
from users import views as user_views
from projects import views as project_views
from django.urls import path, include

urlpatterns = [
    path('', project_views.index, name='home'),
    path('projects/', project_views.projects, name='projects'),
    path('tasks/', user_views.tasks_view, name='tasks'),
    path('login/', user_views.login_view, name='login'),
    path('tasks/', include('tasks.urls')),
]
