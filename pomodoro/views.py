from django.shortcuts import render
from .models import *


def index_view(request):
    return render(request, 'index.html')
