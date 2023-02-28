from django.db import models
from django.utils import timezone


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoItem(models.Model):
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence())

    def __str__(self):
        return f"{self.title}: due {self.due_date}"


