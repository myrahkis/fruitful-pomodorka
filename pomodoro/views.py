from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404


def index_view(request):
    return render(request, 'index.html')


def homework_view(request):
    return render(request, 'homework.html')

