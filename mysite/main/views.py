from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def todolist_index(request):
    todolist_all = ToDoList.objects.all()
    return render(request, "main/todolist_index.html", {"todolists": todolist_all})


def todolist_show_items(request, pk):
    todolist = ToDoList.objects.get(id=pk)
    todolist_items = todolist.item_set.all()

    if request.method == "POST":
        print(request.POST)

        if request.POST.get("save"):

            for item in todolist_items:
                if request.POST.get(f"c{item.id}") == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif request.POST.get("addItem"):
            item_text = request.POST.get("newItem")
            if len(item_text) > 3:
                todolist.item_set.create(text=item_text, complete=False)
            else:
                print("Invalid something")

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
