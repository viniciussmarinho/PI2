from pydantic import BaseModel

class RequestBody(BaseModel):
    name: str
    price: float
    description: str = None