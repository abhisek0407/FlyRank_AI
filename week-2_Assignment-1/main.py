from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel,Field
from typing import Optional
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
app = FastAPI(
    title="Task Management API",
    description="A simple CRUD API built using FastAPI for FlyRank AI Backend Assignment Week-2.",
    version="1.0.0"
)
class taskFormat(BaseModel):
    title:str=Field(...,description="Name of the task",min_length=1)

class taskUpdate(BaseModel):
    title:Optional[str]=Field(default=None,description="Name of the task",min_length=1)
    done:Optional[bool]=Field(default=None,description="Status of the task")

tasks=[
    {
        "id":1,
        "title":"Office work",
        "done":True
    },
    {
        "id":2,
        "title":"Mumbai tour",
        "done":True
    },
    {
        "id":3,
        "title":"Marketing",
        "done":False
    }
]
@app.get(
    "/",
    summary="Root endpoint",
    description="Returns basic information about the Task API."
)
def root():
    return {'name':'Task API','Version':'1.0','endpoints':["/tasks"]}
@app.get(
    "/health",
    summary="Health check",
    description="Checks whether the API server is running."
)
def health():
    return {
        "status":"OK"
    }

@app.get(
    "/tasks",
    summary="Get all tasks",
    description="Returns a list of all available tasks."
)
def view():
    return tasks

@app.get(
    "/tasks/{id}",
    summary="Get task by ID",
    description="Returns a single task using its ID."
)
def get_task(id:int):
    for task in tasks:
        if task["id"]==id:
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error["loc"][1:])
        errors.append({
            "field": field,
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid request body",
            "details": errors
        }
    )

@app.post(
    "/tasks",
    status_code=201,
    summary="Create a new task",
    description="Creates a new task with a unique ID."
)
def add_task(taskInput:taskFormat):
    if taskInput.title.strip() == "":
     raise HTTPException(
        status_code=400,
        detail="Title cannot be empty."
     )
    for task in tasks:
        if task["title"].lower()==taskInput.title.lower():
            raise HTTPException(
                status_code=400,
                detail="Title already exists"
            )
        
    max_id=tasks[-1]["id"]
    new_id=max_id+1
    new_task={
        "id":new_id,
        "title":taskInput.title,
        "done":False
    }
    tasks.append(new_task)
    return new_task

@app.put(
    "/tasks/{id}",
    summary="Update a task",
    description="Updates the title and/or completion status of a task."
)
def update_task(id:int, taskInput:taskUpdate):
    for task in tasks:
        if task["id"]==id:
            if taskInput.title is not None:
                if taskInput.title.strip()=="":
                    raise HTTPException(
                        status_code=400,
                        detail="Title cannot be empty"
                    )
                task["title"]=taskInput.title
            if taskInput.done is not None:
                task["done"]=taskInput.done
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )
    
@app.delete(
    "/tasks/{id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task using its ID."
)
def remove_task(id:int):
    for task in tasks:
        if task["id"]==id:
            tasks.remove(task)
            return
    raise HTTPException(
        status_code=404,
        detail=f"task {id} not found"
    )
    