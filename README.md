# 🚀 FlyRank AI – Backend AI Engineering Internship

Welcome to my internship repository for the **FlyRank AI Backend AI Engineering Internship**.

This repository contains the assignments, hands-on exercises, and backend development projects completed throughout the internship. The work focuses on building practical backend engineering skills using **Python, FastAPI, PostgreSQL, Docker, Supabase, and web scraping**, while developing a strong foundation for AI-powered backend systems.

---

## 👨‍💻 Intern

**Name:** Abhisek Panda  
**Track:** Backend AI Engineering  
**Primary Language:** Python  
**Backend Framework:** FastAPI  

---

## 📂 Repository Structure

```text
FlyRank_AI/
│
├── Week-2 Assignment-1/
│   
│
├── Week-3 Assignment-2/
│  
│
├── Week-3 Assignment-3/
│  
│
├── Week-4 Assignment-4/
│   
│
├── Scraper/
│   ├── src/
│   ├── output/
│   ├── requirements.txt
│   ├── .gitignore
│   └── README.md
│
└── README.md   ← this root README
```

Each assignment is organized in its own folder with the corresponding source code, dependencies, documentation, and project artifacts.

---

## 📌 Assignments

| Assignment | Description | Technologies | Status |
|---|---|---|---|
| Week-2 Assignment-1 | Basic CRUD API for TodoList | Python, FastAPI, Pydantic | ✅ Completed |
| Week-3 Assignment-2 | Connecting CRUD API to a database | Python, FastAPI, PostgreSQL | ✅ Completed |
| Week-3 Assignment-3 | Containerize the backend and database stack | Docker, Docker Compose, FastAPI, PostgreSQL | ✅ Completed |
| Week-4 Assignment-4 | Authentication, login and protected routes | FastAPI, Supabase, JWT, PostgreSQL | ✅ Completed |
| Week-5 Assignment-5(Scraper) | Polite web scraper and data extraction pipeline | Python, Requests, BeautifulSoup, Pydantic | ✅ Completed |

---

## 🛠️ Technologies & Tools

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### Database
- PostgreSQL
- Psycopg
- Supabase

### Authentication
- Supabase Authentication
- JWT Access Tokens
- Bearer Authentication
- FastAPI Authentication Dependencies

### Web Scraping
- Python Requests
- BeautifulSoup4
- HTML Parsing
- URL Discovery
- Page Caching
- Data Normalization
- Pydantic Validation
- Failure Handling
- Run Reporting

### DevOps & Development Tools
- Docker
- Docker Compose
- Git
- GitHub
- VS Code

---

## 📚 Assignment Overview

### 1️⃣ Week-2 Assignment-1 — Basic CRUD API

Built a basic Task/Todo management REST API using FastAPI.

**Key concepts**
- FastAPI application structure
- REST API endpoints
- GET, POST, PUT and DELETE
- Pydantic request validation
- HTTP status codes
- Error handling
- Swagger UI

---

### 2️⃣ Week-3 Assignment-2 — Database Integration

Extended the CRUD API by connecting it to a PostgreSQL database.

**Key concepts**
- PostgreSQL
- Database connections
- SQL queries
- CRUD operations with persistent data
- FastAPI + PostgreSQL integration
- Database-backed REST APIs

---

### 3️⃣ Week-3 Assignment-3 — Containerization

Containerized the application and PostgreSQL database using Docker.

**Key concepts**
- Docker
- Dockerfile
- Docker Compose
- Application containers
- PostgreSQL containers
- Container networking
- Environment variables
- Running a multi-container backend stack

---

### 4️⃣ Week-4 Assignment-4 — Authentication API

Built an authentication system using FastAPI and Supabase.

**Features**
- User signup
- User login
- JWT access token
- Refresh token
- Public routes
- Supabase integration
- Protected routes
- Token verification
- Reusable authentication dependency
- Logout
- Swagger Bearer authentication

**Authentication flow**

```text
Signup
   ↓
Login
   ↓
Access Token
   ↓
Bearer Authentication
   ↓
Reusable Auth Dependency
   ↓
Protected Routes
   ↓
Logout
```

The assignment also included PostgreSQL integration and Docker support.

---

### 5️⃣ Week-5 Assignment-5 — Web Scraping Pipeline

Built a polite and failure-tolerant web scraper for the **Books to Scrape** website.

The scraper processes the first three catalogue pages and discovers **60 unique books**.

**Scraping pipeline**

```text
Catalogue Pages
      ↓
Fetch HTML
      ↓
Cache HTML
      ↓
Discover Book URLs
      ↓
Fetch Book Detail Pages
      ↓
Extract Raw Records
      ↓
Normalize Data
      ↓
Validate with Pydantic
      ↓
books.json
      ↓
run-report.json
```

**Extracted information**

Each validated book record contains:
- Title
- Product URL
- Original price text
- Normalized GBP price
- Availability
- Rating
- Description
- Source catalogue page
- Fetch timestamp

**Reliability features**

The scraper implements:
- Custom User-Agent
- Request timeout
- Request delay
- HTML caching
- HTTP status validation
- Retry for temporary failures
- Handling of individual page failures
- Pydantic record validation
- Duplicate URL prevention
- Idempotent output
- Error logging
- Run reporting

**Output**

```text
output/
├── books.json
├── errors.json
└── run-report.json
```

The scraper is designed so that running it multiple times does not create duplicate records.

**Browser requirement**

No Selenium or browser automation is required for this assignment because the required book information is already present in the HTML returned by the server. Using a browser would only add unnecessary overhead.

---

## ▶️ Running an Assignment

Each assignment contains its own dependencies and instructions.

For example:

```bash
cd "Week-5 Assignment-5"
```

Create a virtual environment:

```bash
python -m venv myenv
```

Activate it on Windows:

```bash
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Then follow the `README.md` inside the individual assignment folder for the assignment-specific run command and configuration.

---

## 🔐 Security

Sensitive credentials and environment variables are not committed to the repository.

Examples of secrets that should remain local include:

```text
.env
API keys
Database credentials
Supabase keys
JWT secrets
```

Environment variables should be stored locally and referenced by the application through configuration.

---

## 📈 Learning Progress

The assignments have progressively covered:

```text
Assignment 1
Basic REST APIs
      ↓
Assignment 2
Database Integration
      ↓
Assignment 3
Docker & Containerization
      ↓
Assignment 4
Authentication & Authorization
      ↓
Assignment 5
Web Scraping & Data Pipelines
```

This progression has helped build practical experience across different areas of backend engineering, from API development and databases to authentication, containerization, and data extraction pipelines.

---

## 🎯 Internship Objective

The objective of this repository is to document my practical learning journey during the **FlyRank AI Backend AI Engineering Internship**.

Through these assignments, I am developing skills in:
- Backend API development
- REST architecture
- Database integration
- Authentication and authorization
- Containerization
- Web scraping
- Data validation and normalization
- Error handling
- Reliable backend workflows
- Git and GitHub
- Writing maintainable backend code

---

## 👨‍💻 Author

**Abhisek Panda**

FlyRank AI – Backend AI Engineering Intern

---

## 📜 License

This repository is maintained for educational and internship purposes.
