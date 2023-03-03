from typing import Optional
from datetime import datetime
from ninja import ModelSchema
from .models import *


class TodoSchema(ModelSchema):
    created: Optional[datetime] = timezone.now()
    status: Optional[str] = "undone"

    class Config:
        model = Todo
        model_fields = ["id", "detail", "created", "status"]


# class AddTodo(ModelSchema):
#     class Config:
#         model = Todo
#         model_fields = ['title']
#
#
# class UpdateTodo(ModelSchema):
#     class Config:
#         model = Todo
#         model_fields = ['id', 'completed']
#
#
# class DeleteTodo(ModelSchema):
#     class Config:
#         model = Todo
#         model_fields = ['id', 'title', 'completed']