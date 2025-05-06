from django.db import models
from django.urls import reverse
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:tag_list')


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ['done', '-created']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('tasks:home')

    def toggle_done(self):
        self.done = not self.done
        self.save()

