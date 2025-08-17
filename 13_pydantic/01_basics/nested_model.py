from typing import List, Optional
from pydantic import BaseModel



class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address
    
    
address = Address(
    street="123",
    city="BSR",
    postal_code="203205"
)

user = User(
    id=1,
    name="Mayank",
    address=address
)


user_data = {
    "id": 1,
    "name": "Mayank",
    "address": {
        "street": "123",
        "city": "BSR",
        "postal_code": "203205"
    }
}

user = User(**user_data)
print(user)