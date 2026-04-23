# 🚀 Task Manager Backend API (24-Hour Sprint)

A professional, secure Task Management API built with **FastAPI** and **SQLAlchemy**. This project demonstrates industry-standard backend architecture including modular file structure, relational databases, and secure JWT authentication.

## 🛠️ Tech Stack
*   **Framework:** FastAPI (Python 3.12+)
*   **Database:** SQLite with SQLAlchemy ORM
*   **Security:** JWT (JSON Web Tokens), OAuth2, and Bcrypt password hashing
*   **Validation:** Pydantic Schemas

## ✨ Key Features
*   **Secure Authentication:** User registration with password hashing (Passlib + Bcrypt).
*   **JWT Authorization:** Protected routes that require a valid Bearer token.
*   **Relational Database:** A one-to-many relationship where users "own" their specific tasks.
*   **Owner-Locked Privacy:** Users can only view, create, or modify tasks linked to their unique User ID.
*   **Automatic Documentation:** Fully interactive API documentation via Swagger UI (/docs).

## 📁 Project Structure
```text
my-backend-api/
├── main.py        # API Routes & Dependency Injection
├── models.py      # SQLAlchemy Database Blueprints
├── schemas.py     # Pydantic Data Validation
├── auth.py        # Security, Hashing, & JWT Logic
├── database.py    # SQL Engine & Session Configuration
└── requirements.txt # Project Dependencies
```

## 🚀 How to Run
1. **Clone the repo:**
   `git clone https://github.com`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Run the server:**
   `fastapi dev main.py`
4. **Access the docs:**
   Open `http://127.0.0` to test the API.
