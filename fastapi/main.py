from fastapi.responses import JSONResponse
from fastapi import FastAPI ,HTTPException 
import uvicorn
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title:str|None=None

app = FastAPI()
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build Task API", "done": True},
    {"id": 3, "title": "Deploy Project", "done": False},
]

@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def get_health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
def get_all_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )
    
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if task.title is None or task.title.strip() == "":
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )
    new_task={
        "id":len(tasks)+1 , 
        "title":task.title , 
        "done":False
    }   
    tasks.append(new_task)

    return new_task 

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)







