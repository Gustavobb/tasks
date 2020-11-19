from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from tasks.models import Task

# Create your views here.
@api_view(["GET"])
def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_task(request):
    return HttpResponse(Task.objects.all())

@api_view(["POST"])
def create_task(request):
    print(request)
    return HttpResponse(request)

@api_view(["POST"])
def delete_task(request, task_id):
    pass

@api_view(["POST"])
def update_task(request, task_id):
    pass