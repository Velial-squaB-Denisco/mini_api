from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from db.database import sql_session
import app.functions as functions
import app.schemas as schemas

app = FastAPI(title="Tasks API")


@app.post("/tasks", response_model=schemas.TaskResponse, status_code=status.HTTP_200_OK)
def create_task(task: schemas.TaskCreate, db: Session = Depends(sql_session.get_db)):
    """Создать задачу"""
    return functions.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def list_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(sql_session.get_db)):
    """Получить список задач"""
    return functions.get_tasks(db, skip=skip, limit=limit)


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(sql_session.get_db)):
    """Получить задачу по ID"""
    task = functions.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}/status", response_model=schemas.TaskResponse)
def update_status(task_id: int, payload: schemas.TaskStatusUpdate, db: Session = Depends(sql_session.get_db)):
    """Изменить статус задачи"""
    task = functions.update_task_status(db, task_id, payload.status)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(sql_session.get_db)):
    """Удалить задачу"""
    functions.delete_task(db, task_id)