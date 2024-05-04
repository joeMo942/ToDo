from django import http
from django.shortcuts import get_object_or_404, redirect, render
from .models import task

def addtask(request):
    taske=request.POST['task']
    task.objects.create(task=taske)
    return redirect('home')


def markascompleted(request,taskid):
    taske=get_object_or_404(task,id=taskid)
    taske.iscompleted=True
    taske.save()
    return redirect('home')


def markasundone(request,taskid):
    taske=get_object_or_404(task,id=taskid)
    taske.iscompleted=False
    taske.save()
    return redirect('home')

def edittask(request,taskid):
    taske=get_object_or_404(task,id=taskid)
    if request.method=='POST':
        newtask=request.POST['new_task']
        taske.task=newtask
        taske.save()
        return redirect('home')
    else:   
        context={
           'tc' : taske,
        }
        return render(request,'edittask.html',context)
    

def deletetask(request,taskid):
    taske=get_object_or_404(task,pk=taskid)
    taske.delete()
    return redirect('home')