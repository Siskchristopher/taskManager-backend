
# Import tools

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database, auth


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

@app.get("/")
def read_root():
    return{"status": "API is online"}

# User Registration Route
@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pwd)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
#

@app.post("/login")
def login(user_credentials: schemas.UserCreate, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()

    if not user or not auth.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    # create Digital ID
    access_token = auth.create_access_token(data={"sub": user.username})
    return {'access_token': access_token, 'token_type': "bearer"}

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
