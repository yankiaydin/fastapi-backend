from pydantic import BaseModel
from typing import Optional

class Department(BaseModel):
    dep_name : str
    manager_name : str

class Personel(BaseModel):
    id : int = Optional
    name: str
    password : str
    position: str = Optional
    department: Department = None




