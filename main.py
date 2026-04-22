
# Import tools

from fastapi import FastAPI

from pydantic import BaseModel

from typing import Optional

# Create app
app = FastAPI()

# Create Model
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

# Temporary local-memory (mimic database)

database = []

#  Route (GET) --> Read root
@app.get("/")
def readRoot():
    return {"message": "Hello World"}

# Route (POST) --> User transmitted data
@app.post("/tasks")
def create_new_Task(task_data: Task):
    database.append(task_data)

    return {"message": "Task Created", "task": task_data}

# Route (GET) --> See Tasks

@app.get("/tasks")
def get_all_Tasks():
    return {"all_tasks": database}
