from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task
from tasks.serializer import TaskSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

def get_tasks(request):
    if request.method == 'GET':
        serializer = TaskSerializer(Task.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)

def get_task(request, task_title):
    if request.method == 'GET':
        try: 
            task = Task.objects.get(pk=task_title)
        except Task.DoesNotExist: 
            raise HttpResponse("Task not found")

        return JsonResponse(task, safe=False, status=201)

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete_task(request, task_title):
    if request.method == 'DELETE':
        try: Task.objects.get(pk=task_title).delete()
        except Task.DoesNotExist: raise HttpResponse("Task not found")

        return HttpResponse("Task deleted")

@csrf_exempt
def delete_tasks(request):
    if request.method == 'DELETE':
        task = Task.objects.all().delete()
        return HttpResponse("Tasks deleted")