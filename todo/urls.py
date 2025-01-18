from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_all_tasks, name='get_all_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/toggle/', views.set_completed, name='set_completed'), 
]
