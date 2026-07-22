from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
app=FastAPI()
class taskFormat(BaseModel):
    id:int=Field(description="Unique identifier assigned to each task")
    title:str=Field(description="Name of the task")
    done:bool=Field(description="Whether task is completed or not")


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
    return HTTPException(
        status_code=404,
        detail=f"Task {id} not found"
    )
        
    
