from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_task(request):
    return HttpResponse(Task.objects.all())

def create_task(request):
    print(request)
    return HttpResponse(request)

def delete_task(request, task_id):
    pass

def update_task(request, task_id):
    pass