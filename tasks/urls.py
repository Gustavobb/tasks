from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTask/<int:task_title>', views.get_task, name='get task'),
    path('getTasks/', views.get_tasks, name='get tasks'),
    path('createTask/', views.create_task, name='create task'),
    path('deleteTask/<int:task_title>', views.delete_task, name='delete task'),
    path('deleteTasks/', views.delete_tasks, name='delete tasks')
]
