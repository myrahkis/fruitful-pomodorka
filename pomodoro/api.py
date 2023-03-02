from ninja import NinjaAPI
from schema import *
from models import *

api = NinjaAPI()

@api.post("/")

