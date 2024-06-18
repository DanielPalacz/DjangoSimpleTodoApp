from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def todolist_index(request):
    todolist_all = ToDoList.objects.all()
    return render(request, "main/todolist_index.html", {"todolists": todolist_all})


def todolist_show_items(request, pk):
    try:
        todolist = ToDoList.objects.get(id=pk)
        todolist_items = todolist.item_set.all()
    except (ToDoList.DoesNotExist, Item.DoesNotExist) as e:
        return HttpResponse(f"<h1>Lack of Todolist number: {pk}. <br>Exception details: {e.args}</h1>")

    return render(request, "main/todolist_items.html",
                  {"todolist": todolist, "todolist_items": todolist_items})


def todolist_create(request):

    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            tdl_name = form.cleaned_data["name"]
            tdl = ToDoList(name=tdl_name)
            tdl.save()
            return HttpResponseRedirect(f"/{tdl.id}")

    else:
        form = CreateNewList()

    return render(request, "main/todolist_create.html", {"form": form})
