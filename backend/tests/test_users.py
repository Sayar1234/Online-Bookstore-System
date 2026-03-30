import pytest
from app.core.security import create_access_token


@pytest.mark.asyncio
async def test_get_users(client):
    response = await client.get("/users/", headers={"Authorization": "Bearer fake_token"})

    assert response.status_code in [200, 401, 403]


@pytest.mark.asyncio
async def test_get_users_no_auth(client):
    response = await client.get("/users/")

    assert response.status_code == 403 or response.status_code == 401


@pytest.mark.asyncio
async def test_admin_routes_require_auth(client):
    response_orders = await client.get("/admin/orders")
    response_sales = await client.get("/admin/sales")

    assert response_orders.status_code in [401, 403]
    assert response_sales.status_code in [401, 403]


@pytest.mark.asyncio
async def test_get_users_authorized_admin(client, test_db):
    admin_doc = {"email": "adminlist@example.com", "password": "pass123", "role": "admin"}
    inserted_admin = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted_admin.inserted_id)})

    response = await client.get("/users/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_admin_orders_sales_with_token(client, test_db):
    admin_doc = {"email": "reports@example.com", "password": "pass123", "role": "admin"}
    inserted_admin = await test_db["users"].insert_one(admin_doc)
    token = create_access_token({"user_id": str(inserted_admin.inserted_id)})

    response_orders = await client.get("/admin/orders", headers={"Authorization": f"Bearer {token}"})
    response_sales = await client.get("/admin/sales", headers={"Authorization": f"Bearer {token}"})

    assert response_orders.status_code == 200
    assert response_sales.status_code == 200
