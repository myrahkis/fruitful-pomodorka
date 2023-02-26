import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitful_pomodorka.settings')

application = get_asgi_application()
