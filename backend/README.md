# Online Bookstore System

A FastAPI-based REST API for managing an online bookstore with user authentication, book management, and order processing.

## Prerequisites

- Python 3.8+
- MongoDB (running on `localhost:27017`)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and update values if needed:

```bash
cp .env.example .env
```

### 3. Connect to MongoDB

Ensure MongoDB is running:

```bash
# On Windows with MongoDB installed
mongod

# Or use Docker
docker run -d -p 27017:27017 mongo:latest
```

### 4. Seed Database

Create admin user:

```bash
python scripts/create_admin.py
```

Seed sample books:

```bash
python scripts/seed_books.py
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 6. API Documentation

Open Swagger UI: `http://localhost:8000/docs`

### 7. Run Tests

```bash
python -m pytest tests/ -v
```

## Default Admin Credentials

- Email: `admin@bookstore.com`
- Password: `admin123`

## Project Structure

```
backend/
├── app/                    # Main application package
│   ├── api/               # API routes
│   ├── controllers/       # Request handlers
│   ├── services/          # Business logic
│   ├── repositories/      # Data access layer
│   ├── models/            # MongoDB models
│   ├── schemas/           # Pydantic schemas
│   ├── core/              # Configuration & security
│   └── main.py            # FastAPI app entry point
├── scripts/               # Utility scripts
├── tests/                 # Test suite
└── requirements.txt       # Dependencies
```
