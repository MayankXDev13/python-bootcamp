from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime



class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    
    
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []
    
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
user = User(
    id=1,
    name="Mayank",
    email="M@mayank.ai",
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="Something",
        city="BSR",
        zip_code="203450"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)


python_dict = user.model_dump()
print(user)
print("=" * 30)
print(python_dict)
print("=" * 30)


json_str = user.model_dump_json()
print(json_str)