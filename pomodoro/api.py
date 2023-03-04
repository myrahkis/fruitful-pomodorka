from typing import List

from ninja import NinjaAPI
from .schema import *
from .models import *
from django.shortcuts import get_object_or_404

api = NinjaAPI()


@api.post("/todo", tags=['Todo'])
def add_todo(request, payload: AddTodo):
    todo = Todo.objects.create(**payload.dict())
    return {"id": todo.id}


@api.get("/todo/{todo_id}", tags=['Todo'], response=DeleteTodo)
def get_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    return todo


@api.patch("/todo/{todo_id}", tags=['Todo'])
def update_todo(request, todo_id: int, payload: UpdateTodo):
    todo = get_object_or_404(Todo, id=todo_id)
    for atr, value in payload.dict().items():
        setattr(todo, atr, value)
    todo.save()
    return {"Success": True}


@api.delete("/todo/{todo_id}", tags=['Todo'])
def delete_todo(request, todo_id: int):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return {"Success": True}


@api.get("/todo", tags=['Todo'], response=List[DeleteTodo])
def list_todo(request):
    todo = Todo.objects.all()
    return todo


