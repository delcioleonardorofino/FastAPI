# 🚀 FastAPI Learning Sandbox

A robust, production-ready REST API boilerplate built as a learning project to master the modern Python backend ecosystem. This project implements asynchronous database transactions, enterprise-grade database migrations, and clean architectural patterns.

---

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous, high-performance)
- **ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (Async engine & declarative mapping)
- **Database Migrations:** [Alembic](https://alembic.alchemycat.org/)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **Data Validation:** [Pydantic v2](https://docs.pydantic.dev/)
- **Environment Management:** Python Dotenv & Pydantic Settings

---

## 🏗️ Architectural Patterns Learned

- **Asynchronous I/O:** Complete async/await pipeline from the HTTP layer down to the database queries.
- **Repository/Service Pattern:** Decoupling business logic from database operations for cleaner, testable code.
- **Dependency Injection:** Leveraging FastAPI's `Depends` for managing database sessions (`AsyncSession`) and authentication lifecycles.
- **Migrations Workflow:** Handling structural database changes safely without losing data using Alembic.

---

## 📂 Project Structure

```text
├── src/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/    # Router paths (e.g., users.py, items.py)
│   │   │   └── api.py          # Main router stitching modules together
│   │   └── deps.py             # Common dependencies (get_db, current_user)
│   ├── core/
│   │   ├── config.py           # Pydantic Settings environment configuration
│   │   └── database.py         # SQLAlchemy async engine and sessionmaker
│   ├── models/                 # SQLAlchemy structural models
│   ├── schemas/                # Pydantic data validation shapes (In/Out)
│   ├── services/               # Business logic / Repository layer
│   └── main.py                 # Application entry point
├── alembic/                    # Database migration environment
│   ├── versions/               # Generated migration scripts
│   └── env.py
├── .env.example                # Template for environment variables
├── alembic.ini                 # Alembic configuration file
├── requirements.txt            # Project dependencies
└── README.md
```
### 🚀 Getting Started
Prerequisites

    Python 3.10+

    PostgreSQL instance running locally or via Docker

### 1. Installation & Environment Setup

Clone the repository and set up your virtual environment:
```Bash

git clone [https://github.com/delcioleonardorofino/FastAPI.git]
cd fastapi-learning-project

python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### Create your .env file based on the template:
```Bash

cp .env.example .env

Open .env and configure your local PostgreSQL connection string:
```
Fragmento do código
```bash
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/your_db_name

    Note: We use asyncpg as the driver to enable full asynchronous database drivers.
```
### 2. Database Migrations (Alembic)

To initialize or apply existing migrations to your database, run:
```Bash

# Apply all current migrations to the database
alembic upgrade head
```
If you make modifications to your SQLAlchemy models in src/models/, generate a new migration file using:
```Bash

alembic revision --autogenerate -m "describe your changes here"
alembic upgrade head
```
### 3. Running the Server

Start the FastAPI application with Uvicorn auto-reload enabled for development:
```Bash

uvicorn src.main:app --reload
```
The server will be running at http://127.0.0.1:8000.
🔍 Interactive Documentation

Once the server is running, you can explore and interact with the API endpoints directly through the browser:

    Swagger UI: http://127.0.0.1:8000/docs (Interactive testing interface)

    ReDoc: http://127.0.0.1:8000/redoc (Clean, structured documentation layout)

## 📄 License

This project is open-source and available under the MIT License.
