from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    # Home page
    path("", views.home, name="home"),

    # Task-related URLs
    path("task/toggle/<int:pk>/", views.toggle_task, name="toggle_task"),
    path("task/add/", views.TaskCreateView.as_view(), name="task_add"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),

    # Tag-related URLs
    path("tags/", views.TagListView.as_view(), name="tag_list"),
    path("tags/add/", views.TagCreateView.as_view(), name="tag_add"),
    path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag_delete"),
]
