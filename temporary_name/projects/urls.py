from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),  # base 'projects/' URL
    path('new/', views.new_project, name='new_project'),
]
