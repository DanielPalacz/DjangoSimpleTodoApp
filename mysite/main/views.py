from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, TodoItem
from .forms import CreateNewList


def index(request, pk):
    todolist = TodoList.objects.get(id=pk)
    # item = todolist.todoitem_set.get(id=1)
    # return HttpResponse(f"<h1>* Hello from v1 [pk={pk}]</h1><h1>* Todolist name: {todolist.name!r} {item.text}</h1>")

    return render(request, "main/list.html", {"todolist": todolist})


def home(request):
    # return HttpResponse("<h1>Hello from home page.</h1>")
    return render(request, "main/home.html", {"name": "test"})


def create(request):

    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()

            return HttpResponseRedirect(f"/{t.id}")

    else:
        # request.method == "GET"
        form = CreateNewList()

    return render(request, "main/create.html", {"form": form})
