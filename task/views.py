from django.http import Http404
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task, Category


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)
            return redirect('task_all')
    else:
        form = TaskForm()
    return render(request, 'task/task_add.html', {'form': form})


def task_all(request):
    tasks = Task.objects.all()
    cats = Category.objects.all()

    context = {
        'tasks': tasks,
        'cats': cats,
        'title': 'Task List',
        'cat_selected': 0,
    }

    return render(request, 'task/task_all.html', context)


def show_category(request, cat_id):
    tasks = Task.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(tasks) == 0:
        raise Http404()

    context = {
        'tasks': tasks,
        'cats': cats,
        'title': 'Category view',
        'cat_selected': cat_id,
    }

    return render(request, 'task/task_all.html', context=context)
