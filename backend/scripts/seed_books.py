import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.mongo_client import connect_to_mongo, close_mongo_connection, get_database
from app.models.book_model import book_model


SAMPLE_BOOKS = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "price": 12.99,
        "stock": 25
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "price": 14.99,
        "stock": 30
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "price": 13.99,
        "stock": 20
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 11.99,
        "stock": 35
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "price": 10.99,
        "stock": 28
    },
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "price": 16.99,
        "stock": 40
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "price": 24.99,
        "stock": 15
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "price": 15.99,
        "stock": 22
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "price": 18.99,
        "stock": 18
    },
    {
        "title": "Neuromancer",
        "author": "William Gibson",
        "price": 13.99,
        "stock": 12
    }
]


async def seed_books():
    try:
        await connect_to_mongo()

        db = get_database()
        books_collection = db["books"]

        existing_count = await books_collection.count_documents({})
        if existing_count > 0:
            print(f"✓ Database already has {existing_count} books. Skipping seeding.")
            return

        book_documents = []
        for book_data in SAMPLE_BOOKS:
            book_doc = book_model(book_data)
            book_documents.append(book_doc)

        result = await books_collection.insert_many(book_documents)

        print("Successfully seeded database with sample books!")
        print(f"  Added {len(result.inserted_ids)} books:")
        for i, book in enumerate(SAMPLE_BOOKS, 1):
            print(f"    {i}. '{book['title']}' by {book['author']} - ${book['price']} (Stock: {book['stock']})")

    except Exception as e:
        print(f"Error seeding books: {str(e)}")
        sys.exit(1)
    finally:
        await close_mongo_connection()


if __name__ == "__main__":
    print("Seeding books...")
    asyncio.run(seed_books())
    print("Done!")