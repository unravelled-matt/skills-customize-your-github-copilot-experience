from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    title: str


tasks: list[dict] = []


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Task API"}


@app.get("/tasks")
def list_tasks() -> list[dict]:
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate) -> dict:
    new_task = {"id": len(tasks) + 1, "title": task.title}
    tasks.append(new_task)
    return new_task
