from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

from .models import TasksList, Task
from .forms import TasksListForm, TaskForm


@login_required
def tasks_lists(request):
    lists = request.user.tasks_lists_owner.all()
    return render(request, "taskslists/taskslists.html",
                  {"lists": lists})


@login_required
def new_tasks_list(request):
    if request.method == "POST":
        tasks_list = TasksList(owner=request.user)
        form = TasksListForm(instance=tasks_list, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_lists")
    else:
        form = TasksListForm()
    return render(request, "taskslists/new_tasks_list_form.html",
                  {'form': form})


@login_required
def view_tasks_list(request, id):
    tasks_list = get_object_or_404(TasksList, pk=id)
    if not request.user == tasks_list.owner:
        raise PermissionDenied
    tasks = tasks_list.list_tasks.all()
    return render(request, "taskslists/tasks_list.html", {
        "tasks_list": tasks_list,
        "tasks": tasks,
    })


@login_required
def edit_tasks_list(request, id, task_id):
    tasks_list = get_object_or_404(TasksList, pk=id)
    if not request.user == tasks_list.owner:
        raise PermissionDenied
    tasks = tasks_list.list_tasks.all()
    print(type(task_id))
    if task_id != "0":
        task = get_object_or_404(Task, pk=task_id)
        if not task.tasks_list == tasks_list:
            raise PermissionDenied
    else:
        task = Task(tasks_list=tasks_list)
    if request.method == "POST":
        print("POST")
        if "edit" in request.POST:
            form = TaskForm(instance=task, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect("edit_tasks_list", id=tasks_list.pk, task_id=0)
    else:
        form = TaskForm(instance=task)
    return render(request, "taskslists/edit_tasks_list.html",
                  {'form': form,
                   'tasks_list': tasks_list,
                   'tasks': tasks,
                   'task_id': task_id})


@login_required
def scratch_task(request, id, task_id):
    tasks_list = get_object_or_404(TasksList, pk=id)
    if not request.user == tasks_list.owner:
        raise PermissionDenied
    task = get_object_or_404(Task, pk=task_id)
    if not task.tasks_list == tasks_list:
        raise PermissionDenied
    task.done = task.done ^ True
    task.save()
    return redirect("view_tasks_list", id=id)
