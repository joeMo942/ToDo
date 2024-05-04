from django.urls import  path
from . import views
urlpatterns=[

    path('addtask/',views.addtask,name="addtask"),
    path('markascompleted/<int:taskid>/',views.markascompleted,name="markascompleted"),
    path('markasundone/<int:taskid>/',views.markasundone,name="markasundone"),
    path('edittask/<int:taskid>/',views.edittask,name="edittask"),
    path('deletetask/<int:taskid>/',views.deletetask,name="deletetask"),

]