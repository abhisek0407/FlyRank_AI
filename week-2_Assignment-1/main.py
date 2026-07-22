from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel,Field
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
app=FastAPI()
class taskFormat(BaseModel):
    title:str=Field(...,description="Name of the task",min_length=1)


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
@app.get("/")
def root():
    return {'name':'Task API','Version':'1.0','endpoints':["/tasks"]}
@app.get("/health")
def health():
    return {
        "status":"OK"
    }

@app.get("/tasks")
def view():
    return tasks

@app.get("/tasks/{id}")
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

@app.post("/tasks",status_code=201)
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

        

