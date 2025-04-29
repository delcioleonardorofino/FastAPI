from fastapi import FastAPI, Response, status, Depends
from fastapi.params import Body
from crud import (get_completed_tasks, get_tasks, get_uncompleted_tasks, create_task, complete_task, delete_task)
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

   
@app.get('/tasks', status_code=status.HTTP_200_OK)
def get_tasks(db: Session = depends(get_db)):
    posts  =  db.query(models.Task).all()
    return {"Data" : posts}

@app.get("/tasks/completed", status_code=status.HTTP_200_OK)
def read_completed():
    return get_completed_tasks()

@app.get("/tasks/uncomplete")
def read_uncompleted():
    return get_uncompleted_tasks()

@app.post("tasks/create", status_code=status.HTTP_201_CREATED)
def crt_task():
    return create_task()

@app.patch('tasks/comptask{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(id):
    return complete_task(id)

@app.delete("/tasks/deletask{id}")
def del_task(id):
    return delete_task(id)