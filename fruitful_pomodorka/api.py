from ninja import NinjaAPI
from pomodoro.api import router as todos_router

api = NinjaAPI()

api.add_router("/todos/", todos_router)
