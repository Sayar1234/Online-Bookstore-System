import pytest
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_create_order_anonymous(client):
    response = await client.get("/orders/", headers={"Authorization": "Bearer fake_token"})

    assert response.status_code in [401, 403]


@pytest.mark.asyncio
async def test_place_and_get_order(client, test_db):
    # Create a test book directly in DB (admin bypass)
    book = {
        "title": "Order Book",
        "author": "Writer",
        "description": "Orderable",
        "price": 15.0,
        "stock": 10
    }
    result = await test_db["books"].insert_one(book)
    book_id = str(result.inserted_id)

    # create user and token directly to avoid bcrypt backend unpredictability
    user_doc = {
        "email": "orderuser@example.com",
        "password": "pass123",
        "role": "customer"
    }
    inserted_user = await test_db["users"].insert_one(user_doc)
    user_id = str(inserted_user.inserted_id)
    token = create_access_token({"user_id": user_id})

    place_response = await client.post(
        "/orders/",
        json={"items": [{"book_id": book_id, "quantity": 1}]},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert place_response.status_code == 200
    order_id = place_response.json().get("order_id")
    assert order_id is not None

    detail_response = await client.get(
        f"/orders/{order_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert detail_response.status_code == 200
    assert detail_response.json()["order"]["user_id"] is not None


@pytest.mark.asyncio
async def test_order_invalid_book(client, test_db):
    admin_doc = {"email": "orderadmin@books.com", "password": "pass123", "role": "admin"}
    inserted_admin = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted_admin.inserted_id)})

    user_doc = {"email": "customer1@example.com", "password": "pass123", "role": "customer"}
    inserted_user = await test_db["users"].insert_one(user_doc)
    user_token = create_access_token({"user_id": str(inserted_user.inserted_id)})

    response = await client.post(
        "/orders/",
        json={"items": [{"book_id": "000000000000000000000000", "quantity": 1}]},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_order_insufficient_stock(client, test_db):
    book = {"title": "Limited", "author": "A", "description": "D", "price": 5.0, "stock": 1}
    book_id = str((await test_db["books"].insert_one(book)).inserted_id)

    user_doc = {"email": "customer2@example.com", "password": "pass123", "role": "customer"}
    inserted_user = await test_db["users"].insert_one(user_doc)
    user_token = create_access_token({"user_id": str(inserted_user.inserted_id)})

    response = await client.post(
        "/orders/",
        json={"items": [{"book_id": book_id, "quantity": 5}]},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert response.status_code == 400
