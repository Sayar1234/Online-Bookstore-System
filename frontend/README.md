# Online Bookstore Frontend (React + Vite)

This directory holds the frontend for the Online Bookstore System.

## Setup

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## Build

```bash
npm run build
```

## Test

No frontend tests currently included.

## Structure

- `src/pages`: page-level views (Books, Cart, Orders, Admin, etc.)
- `src/components`: UI parts (BookCard, Navbar, Modal, etc.)
- `src/api`: axios API layer for auth, books, orders
- `src/context`: Auth and Cart contexts
- `src/hooks`: reusable hooks (useFetch, useAuth, useCart)
