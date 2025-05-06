from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, Tag
from .forms import TaskForm, TagForm
from django.urls import reverse_lazy

def home(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"tasks": tasks})

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.toggle_done()
    return redirect("tasks:home")

class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"

class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag_list")

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:tag_list")

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag_list")

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:home")

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:home")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:home")

