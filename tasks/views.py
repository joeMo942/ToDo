from django import http
from django.shortcuts import redirect, render
from .models import task

def addtask(request):
    taske=request.POST['task']
    task.objects.create(task=taske)
    return redirect('home')
