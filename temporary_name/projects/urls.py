from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),  # base 'projects/' URL
    path('new/', views.new_project, name='new_project'),
    path('<int:pk>/', views.project_detail, name='project_detail'), 
]
