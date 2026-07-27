# Task Management API

A simple RESTful Task Management API built using **FastAPI** as part of the **FlyRank AI Backend Engineering Internship – Week 2 Assignment 1**.

The project demonstrates a complete CRUD API using in-memory storage and automatic API documentation with Swagger UI.

---

## Features

- Create a task
- View all tasks
- View a task by ID
- Update a task
- Delete a task
- Request validation
- Custom error handling
- Swagger UI documentation

---

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/FlyRank_AI.git
```

Move to the assignment folder.

```bash
cd FlyRank_AI/week-2_Assignment-1
```

Create a virtual environment.

```bash
python -m venv myenv
```

Activate it.

Windows

```bash
myenv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn main:app --reload
```

The API will start at

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Root endpoint |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

---

## Sample curl Output

### Create a Task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Buy Milk\"}"
```

Example response

```http
HTTP/1.1 201 Created

{
    "id":4,
    "title":"Buy Milk",
    "done":false
}
```

---

## Swagger UI

Open

```
http://127.0.0.1:8000/docs
```

Insert your Swagger UI screenshot here.

Example:

```
![Swagger UI](images/swagger-ui.png)
```

(or simply paste the image directly into GitHub while editing README.)

---

## Project Structure

```
week-2_Assignment-1/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Author

**Abhisek Panda**

Backend AI Engineering Intern

FlyRank AI