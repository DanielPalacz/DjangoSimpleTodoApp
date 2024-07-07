from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList, TodoItem
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello from index page.</h1>")


def v1(request, pk):
    todolist = TodoList.objects.get(id=pk)
    item = todolist.todoitem_set.get(id=1)
    return HttpResponse(f"<h1>* Hello from v1 [pk={pk}]</h1><h1>* Todolist name: {todolist.name!r} -> {item.text}</h1>")
