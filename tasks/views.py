from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from tasks.serializer import TaskSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    if request.method == 'GET':
        return HttpResponse(Task.objects.all())

def create_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =TaskSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status =201)
        return JsonResponse(serializer.errors, status = 400)


def delete_task(request, task_id):
    pass

def update_task(request, task_id):
    pass