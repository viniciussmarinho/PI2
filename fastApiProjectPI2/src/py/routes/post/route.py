from fastapi import APIRouter
from src.py.routes.db import items_db, RequestBody

router_post = APIRouter()

@router_post.post("/items/")
def create_item(item: RequestBody):
    items_db.append(item)
    return {"message": "Item adicionado com sucesso", "item": item}
