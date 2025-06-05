from django.contrib import admin
from django.urls import path, include
#from tasks import views as task_views
from projects import views as project_views
from users import views as user_views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_views.index, name='index'),  # sākuma lapa ar pogām
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('login/', user_views.login_view, name='login'),
    path('projects/', project_views.projects, name='projects'),
    # Šī rinda izņemta, jo tasks aplikācija nav importēta vai nav pieejama
    # path('tasks/', task_views.tasks, name='tasks'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('comments/', include('comments.urls')),
    path('timelogs/', include('timelogs.urls')),
    path('files/', include('files.urls')),
]
