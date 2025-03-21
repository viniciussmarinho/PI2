from fastapi import APIRouter
from src.py.routes.db import items_db

router_get = APIRouter()

@router_get.get("/items/")
def list_items():
    return items_db
