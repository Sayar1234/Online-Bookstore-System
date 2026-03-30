# Online Bookstore System

Central repository for the Online Bookstore System, which includes:

- `backend/`: FastAPI + MongoDB REST API implementation
- `frontend/`: React + Vite client UI

## Overview

The system provides:

- User authentication (JWT)
- Admin/bookstore management
- Book browse/search
- Cart management and order checkout
- Order history and admin order status

## Quickstart

### 1. Backend

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# adjust .env values if necessary
python scripts/create_admin.py
python scripts/seed_books.py
uvicorn app.main:app --reload
```

API docs: `http://localhost:8000/docs`

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

UI: `http://localhost:5173`

## Testing

Backend tests:

```bash
cd backend
pytest -v
```

## Default admin

- Email: `admin@bookstore.com`
- Password: `admin123`

## Repo structure

- `backend/` - FastAPI service with controllers, services, repos
- `frontend/` - React UI with pages, components, context

## Tech stack

- Python 3.8+, FastAPI, Motor, Pydantic, PyMongo
- Node 18+, React, Vite, Axios
- MongoDB for storage
