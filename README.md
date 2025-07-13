#  Notes API with FastAPI & JWT Auth

A secure REST API built using FastAPI, PostgreSQL, and SQLAlchemy. Features:

-  JWT authentication
-  User registration/login
-  Create, update, delete notes
-  Notes are private (user-specific)
-  PostgreSQL + SQLAlchemy ORM
-  Fully testable via Swagger Docs (`/docs`)

##  Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT (via python-jose)
- Bcrypt

##  How to Run Locally

```bash
git clone <your-repo-url>
cd <project-folder>
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
