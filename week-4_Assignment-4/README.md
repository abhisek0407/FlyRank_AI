# 🚀 FlyRank AI – Week 3 Assignment 3

A Task Management REST API built using **FastAPI** and **PostgreSQL**, containerized with **Docker** and orchestrated using **Docker Compose**.

This project demonstrates a complete CRUD API with PostgreSQL as the database backend and Docker Compose to start both the API and database using a single command.

---

## 👨‍💻 Author

**Name:** Abhisek Panda

**Track:** Backend AI Engineering Internship

**Framework:** FastAPI

**Database:** PostgreSQL

---

## 🛠️ Tech Stack

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Docker
- Docker Compose
- Pydantic
- Uvicorn

---

# 📁 Project Structure

```
week-3_Assignment-3/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .env.example
├── README.md
└── images/
    ├── swagger.png
    └── postgres.png
```

---

# ⚙️ Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
DATABASE_URL=postgres://postgres:dev@localhost:5432/tasks
```

When running with **Docker Compose**, the API automatically uses:

```text
postgres://postgres:dev@db:5432/tasks
```

configured in `compose.yaml`.

---

# ▶️ Run the Project

## Build and start the complete stack

```bash
docker compose up --build
```

This command automatically:

- Starts PostgreSQL
- Builds the FastAPI image
- Starts the API server
- Connects the API to PostgreSQL

---

## Stop the application

```bash
docker compose down
```

---

## API URLs

Root

```
http://localhost:8000
```

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

# Example cURL

```bash
curl -i -X GET http://localhost:8000/tasks
```

Example Response

```http
HTTP/1.1 200 OK
content-type: application/json

[
  {
    "id":1,
    "title":"Office work",
    "done":true
  },
  {
    "id":2,
    "title":"Mumbai tour",
    "done":true
  },
  {
    "id":3,
    "title":"Marketing",
    "done":false
  }
]
```

---

# Screenshots

## Swagger UI

![Swagger UI](images/swagger.png)

---

## PostgreSQL Database

![PostgreSQL](images/postgres.png)

---

# Features

- PostgreSQL database
- Full CRUD operations
- Input validation
- Custom validation error handling
- Dockerized FastAPI application
- Docker Compose support
- Persistent database using Docker Volumes
- Environment variable configuration

---

# Docker Volume Persistence

Data is stored inside the Docker volume.

Stopping the containers using

```bash
docker compose down
```

does **not** delete the stored tasks.

Running

```bash
docker compose up
```

again restores all previously created tasks.

---

# Assignment Stages Completed

- ✅ Stage 0 – PostgreSQL in Docker
- ✅ Stage 1 – Connect via `.env`
- ✅ Stage 2 – Read data from PostgreSQL
- ✅ Stage 3 – Full CRUD on PostgreSQL
- ✅ Stage 4 – Docker Compose for complete stack

---

# License

This project was developed for the **FlyRank AI Backend AI Engineering Internship** as part of the Week 3 Assignment.