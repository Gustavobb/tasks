from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/', views.get_tasks, name='get tasks'),
    path('create/', views.create_task, name='create task'),
    path('delete/<int:task_id>', views.delete_task, name='delete task'),
    path('update/<int:task_id>', views.update_task, name='update task')
]
