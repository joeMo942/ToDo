# from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import task

def home(request):
    tasksdone=task.objects.filter(iscompleted=True)
    tasksnotdone = task.objects.filter(iscompleted=False) 
    context = {'tasksdone':tasksdone,'tasksnotdone':tasksnotdone}
    return render(request, 'home.html',context)