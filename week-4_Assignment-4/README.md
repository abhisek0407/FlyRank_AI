# 🔐 Authentication API using FastAPI, PostgreSQL & Supabase

A secure REST API built with **FastAPI**, **PostgreSQL**, and **Supabase Authentication**. This project demonstrates user authentication using JWT tokens, protected routes, reusable authentication middleware (dependency), PostgreSQL integration, and interactive API documentation with Swagger UI.

---

## 🚀 Features

- User Signup with Supabase Authentication
- User Login with JWT Access & Refresh Tokens
- Public Route (No Authentication Required)
- Protected Routes using JWT Authentication
- Reusable Authentication Dependency
- User Logout
- PostgreSQL Database Integration
- Swagger UI with Bearer Token Authentication
- Docker Support
- Environment Variable Configuration

---

## 🛠️ Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- Supabase Authentication
- Psycopg
- Docker & Docker Compose
- Swagger UI (OpenAPI)

---

## 📁 Project Structure

```
week-4_Assignment-4/
│
├── main.py
├── auth.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root using the following format:

```env
DATABASE_URL=postgres://postgres:dev@localhost:5432/tasks
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_supabase_anon_key
```

> **Important:** Never commit your `.env` file to GitHub.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd week-4_Assignment-4
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
myenv\Scripts\activate
```

#### Linux / macOS

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐳 Start PostgreSQL using Docker

```bash
docker compose up -d
```

Verify the container is running:

```bash
docker compose ps
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📚 API Reference

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| POST | `/auth/signup` | ❌ No | Register a new user |
| POST | `/auth/login` | ❌ No | Login and receive JWT tokens |
| POST | `/auth/logout` | ✅ Yes | Logout current user |
| GET | `/public/info` | ❌ No | Public endpoint |
| GET | `/protected/profile` | ✅ Yes | Returns authenticated user's profile |
| GET | `/protected/dashboard` | ✅ Yes | Protected dashboard endpoint |
| GET | `/tasks` | ❌ No | Retrieve all tasks |
| GET | `/tasks/{id}` | ❌ No | Retrieve task by ID |
| POST | `/tasks` | ❌ No | Create a new task |
| PUT | `/tasks/{id}` | ❌ No | Update an existing task |
| DELETE | `/tasks/{id}` | ❌ No | Delete a task |

---

# 🔑 Authentication

Protected routes require a valid JWT Access Token.

Example Authorization header:

```http
Authorization: Bearer <your_access_token>
```

You can obtain the Access Token by logging in through:

```
POST /auth/login
```

---

# 📖 Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Click **Authorize**, paste your JWT Access Token, and test protected endpoints directly from the browser.

---

# 📸 Swagger UI Screenshot

> Replace the image below with your own screenshot after completing the project.

```text
docs/swagger-ui.png
```

Example:

```markdown
![Swagger UI](images/Screenshot 2026-08-07 212816.png)
```

---

# 🧪 Sample Workflow

1. Register a new user using `/auth/signup`
2. Login using `/auth/login`
3. Copy the Access Token
4. Click **Authorize** in Swagger UI
5. Paste the Access Token
6. Access protected endpoints
7. Logout using `/auth/logout`

---

# 📋 Requirements

```
fastapi
uvicorn
psycopg[binary]
python-dotenv
supabase
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Abhisek Panda**

Backend Authentication API built as part of the **FlyRank AI Backend Engineering Internship – Week 4 Assignment**.

---

# 📄 License

This project is created for educational and internship assignment purposes.