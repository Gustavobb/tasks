from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getTasks/', views.get_tasks, name='get tasks'),
    path('createTask/', views.create_task, name='create task'),
    path('deleteTasks/', views.delete_tasks, name='delete tasks')
]
