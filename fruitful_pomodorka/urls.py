from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from fruitful_pomodorka import settings
from pomodoro import views
from pomodoro.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('todo/', views.pomodorka_view),
    path('api/', api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
