from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import *


def index_view(request):
    return render(request, 'index.html', {'todos': Todo.objects.all()})


# def pomodorka_view(request):
#     return render(request, 'index.html', {'todos': Todo.objects.all()})

def todo_view(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'index.html', {'todo': todo})



