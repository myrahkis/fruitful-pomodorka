from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)


class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250)


# class TodoManager(models.Manager):
#     def to_list(self):
#         return [todo.to_json() for todo in self.get_queryset()]
#
#
# class Todo(models.Model):
#     STATUS_CHOICES = [
#         ("done", "done"),
#         ("undone", "undone"),
#     ]
#     detail = models.CharField(max_length=500)
#     created = models.DateField(default=timezone.now, null=False)
#     status = models.CharField(max_length=100, null=True, blank=True, choices=STATUS_CHOICES)
#     updated = models.DateField(default=timezone.now, null=False)
#
#     objects = TodoManager()
#
#     def to_json(self):
#         return {
#             "id": self.id,
#             "created": self.created.strftime("%Y-%m-%d"),
#             "detail": self.detail,
#             "status": self.status,
#         }

