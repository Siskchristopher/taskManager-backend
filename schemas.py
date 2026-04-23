
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# User tasks --> what user sends
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

# Origin response --> sent to user
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    owner_id: int

    class Config:
      from_attributes = True


