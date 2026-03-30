import pytest
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_get_books(client):
    response = await client.get("/books/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_book_by_id_not_found(client):
    response = await client.get("/books/000000000000000000000000")

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_create_book_unauthorized(client):
    response = await client.post(
        "/books/",
        json={
            "title": "Test Book",
            "author": "Author",
            "description": "Desc",
            "price": 10.0,
            "stock": 5
        }
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_book_admin(client, test_db):
    admin_doc = {"email": "admin@books.com", "password": "pass123", "role": "admin"}
    inserted = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted.inserted_id)})

    response = await client.post(
        "/books/",
        json={"title": "Admin Book", "author": "Admin", "description": "Desc", "price": 20.0, "stock": 5},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200 or response.status_code == 201


@pytest.mark.asyncio
async def test_update_book_admin(client, test_db):
    admin_doc = {"email": "updater@books.com", "password": "pass123", "role": "admin"}
    inserted_admin = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted_admin.inserted_id)})

    book = {"title": "Old", "author": "A", "description": "D", "price": 10.0, "stock": 5}
    book_id = str((await test_db["books"].insert_one(book)).inserted_id)

    update_response = await client.put(
        f"/books/{book_id}",
        json={"title": "New", "author": "A", "price": 12.5, "stock": 5},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert update_response.status_code == 200


@pytest.mark.asyncio
async def test_delete_book_admin(client, test_db):
    admin_doc = {"email": "deleter@books.com", "password": "pass123", "role": "admin"}
    inserted_admin = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted_admin.inserted_id)})

    book = {"title": "Delete", "author": "A", "description": "D", "price": 10.0, "stock": 5}
    book_id = str((await test_db["books"].insert_one(book)).inserted_id)

    delete_response = await client.delete(
        f"/books/{book_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert delete_response.status_code == 200
