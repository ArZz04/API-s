from pydantic import BaseModel

class Product(BaseModel):
    plu: str
    name: str
    price: str