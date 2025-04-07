from fastapi import FastAPI
from models import Task

app = FastAPI()
tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Task added"}

@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return {"message": "Task completed"}
    return {"error": "Task not found"}
