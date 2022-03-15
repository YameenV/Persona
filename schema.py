from typing import List, Optional
from pydantic import BaseModel

class CreateUser (BaseModel):
    email : str
    password : str

    class Config:
        orm_mode = True