from typing import Optional
from pydantic import BaseModel, Field
import re


class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # three dot means required field
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Mayank"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000        
    )
    
    
class User(BaseModel):
    email: str = Field(..., regix=r"")
    phone: str = Field(..., regix=r"")
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in Years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )