from pydantic import BaseModel
from typing import Optional
from datetime import date

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False
    deadline: Optional[date] = None
