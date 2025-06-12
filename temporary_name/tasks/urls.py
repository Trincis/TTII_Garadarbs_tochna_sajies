from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),  # make sure views.tasks exists!
]
