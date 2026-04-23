
# Import tools

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

# Table creation
models.base.metadata.create_all(bind=database.engine)

# Create app
app = FastAPI()
 # Opens Connection
def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

# Route (POST) --> User transmitted data
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_new_task(task_data: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(title=task_data.title, description=task_data.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# Route (GET) --> See Tasks

@app.get("/tasks")
def get_all_Tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return {"all_tasks": tasks}
