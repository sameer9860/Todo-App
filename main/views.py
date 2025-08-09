from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.db.models import Q
from django.contrib import messages

def task_list(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')

    tasks = Task.objects.all()

    if query:
        tasks = tasks.filter(title__icontains=query)

    if status_filter == 'completed':
        tasks = tasks.filter(completed=True)
    elif status_filter == 'pending':
        tasks = tasks.filter(completed=False)

    context = {
        'tasks': tasks,
        'query': query or '',
        'status_filter': status_filter or '',
    }
    return render(request, 'main/task_list.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'main/task_form.html', {'form': form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated!")
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'main/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted!")
        return redirect('task_list')
    return render(request, 'main/task_confirm_delete.html', {'task': task})
