from fastapi import FastAPI,HTTPException,Request
from pydantic import BaseModel,Field
from typing import Optional
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import psycopg
from dotenv import load_dotenv
load_dotenv()
import os
DATABASE_URL=os.getenv("DATABASE_URL")
conn=psycopg.connect(DATABASE_URL)
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
        id SERIAL PRIMARY KEY,
        title TEXT,
        done BOOLEAN
)
""")
cursor.execute("SELECT count(*) FROM tasks")
count=cursor.fetchone()[0]
if count==0:
    cursor.execute("""
INSERT INTO tasks(title,done)
VALUES
   ('Office work',TRUE),
   ('Mumbai tour',TRUE),
   ('Marketing',FALSE);
""")
    conn.commit()
app = FastAPI(
    title="Task Management API",
    description="Task Management API using FastAPI and PostgreSQL for FlyRank AI Week 3 Assignment 3.",
    version="1.0.0"
)
class taskFormat(BaseModel):
    title:str=Field(...,description="Name of the task",min_length=1)

class taskUpdate(BaseModel):
    title:Optional[str]=Field(default=None,description="Name of the task",min_length=1)
    done:Optional[bool]=Field(default=None,description="Status of the task")

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
    cursor.execute("SELECT * FROM tasks")
    data=cursor.fetchall()
    return data

@app.get(
    "/tasks/{id}",
    summary="Get task by ID",
    description="Returns a single task using its ID."
)
def get_task(id:int):
    cursor.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    task = cursor.fetchone()
    if task:
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
    cursor.execute("SELECT * FROM tasks where title=%s",(taskInput.title,))
    result=cursor.fetchone()
    if result:
        raise HTTPException(
            status_code=400,
            detail="Title already exists"
        )
        
    
    cursor.execute("INSERT INTO tasks(title,done) VALUES (%s,%s) RETURNING id",(taskInput.title,False))
    new_id=cursor.fetchone()[0]
    conn.commit()
    return {
    "id": new_id,
    "title": taskInput.title,
    "done": False
}

@app.put(
    "/tasks/{id}",
    summary="Update a task",
    description="Updates the title and/or completion status of a task."
)
def update_task(id:int, taskInput:taskUpdate):
    cursor.execute("SELECT * FROM tasks WHERE id=%s",(id,))
    result=cursor.fetchone()
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"Task {id} not found"
        )
    
    if taskInput.title is not None:
        if taskInput.title.strip()=="":
            raise HTTPException(
                status_code=400,
                detail="Title cannot be empty"
            )
        cursor.execute("UPDATE tasks SET title=%s WHERE id=%s",(taskInput.title,id))
    if taskInput.done is not None:
        cursor.execute("UPDATE tasks SET done=%s WHERE id=%s",(taskInput.done,id))
    conn.commit()

    cursor.execute("SELECT * FROM tasks WHERE id=%s", (id,))
    updated_task = cursor.fetchone()

    return {
        "id": updated_task[0],
        "title": updated_task[1],
        "done": bool(updated_task[2])
    }
   
    
@app.delete(
    "/tasks/{id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task using its ID."
)
def remove_task(id:int):
    cursor.execute("DELETE FROM tasks WHERE id=%s",(id,))
    if cursor.rowcount==0:
     raise HTTPException(
            status_code=404,
            detail=f"task {id} not found"
        )
    conn.commit()
    return
    
    