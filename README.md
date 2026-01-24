# 🚀 FastAPI REST API Backend Project

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/FastAPI-Backend-green.svg)](https://fastapi.tiangolo.com/)
[![ORM](https://img.shields.io/badge/ORM-SQLAlchemy-orange.svg)](https://www.sqlalchemy.org/)
[![Stars](https://img.shields.io/github/stars/zufran123/<your-repo-name>.svg?style=social)](https://github.com/zufran123/<your-repo-name>/stargazers)
[![Forks](https://img.shields.io/github/forks/zufran123/<your-repo-name>.svg?style=social)](https://github.com/zufran123/<your-repo-name>/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/zufran123/<your-repo-name>.svg)](https://github.com/zufran123/<your-repo-name>/commits/main)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=zufran123.fastapi-backend)

---

This project is a structured REST API backend built using **FastAPI**, **SQLAlchemy**, and **Pydantic**.  
It demonstrates complete **CRUD operations**, **database integration**, **dependency injection**, **basic authentication**, and **proper error handling** following a clean backend architecture used in real-world applications.

---

## 🧱 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy ORM**
- **Pydantic**
- **SQLite**
- **Uvicorn**

---

## 📁 Project Structure

```
.
├── main.py          # FastAPI app & routes
├── database.py      # DB engine, session management
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── crud.py          # Database operations (CRUD)
├── auth.py          # Basic authentication dependency
├── requirements.txt
└── README.md
```

---

## 🔍 Key Features

- REST API built with FastAPI
- SQLAlchemy ORM with relational database
- Pydantic request and response validation
- Full CRUD operations
- Dependency Injection using `Depends`
- Basic route protection with authentication
- Proper HTTP error handling
- Automatic interactive API docs (Swagger & ReDoc)
- Clean modular backend structure

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/zufran123/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Open in browser:  
http://127.0.0.1:8000

---

## 📘 API Documentation

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 📌 Example Endpoints (User Resource)

| Method | Endpoint       | Description      |
|-------|----------------|------------------|
| POST  | /users         | Create user      |
| GET   | /users         | Get all users    |
| GET   | /users/{id}    | Get user by ID   |
| PUT   | /users/{id}    | Update user      |
| DELETE| /users/{id}    | Delete user      |

---

## ❗ Error Handling

- Proper HTTP status codes
- Validation errors handled via Pydantic
- Custom error messages for invalid operations

---

## 💡 What This Project Demonstrates

- FastAPI request lifecycle
- Dependency Injection in real APIs
- ORM integration with SQLAlchemy
- Schema validation with Pydantic
- Clean backend project organization

---

## 🚀 Future Improvements

- JWT Authentication
- Role Based Access Control (RBAC)
- Pagination, Filtering, Sorting
- PostgreSQL/MySQL integration
- Dockerization for deployment

---

## 👨‍💻 Author

**Mohd Zufran**  
[![LinkedIn: mohdzufran](https://img.shields.io/badge/LinkedIn-mohdzufran-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/mohdzufran)

---

## 📄 License

This project is licensed under the **MIT License**.  
Please include proper credit if you use or modify this project.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
