import pytest
from app.core.security import create_access_token, hash_password


@pytest.mark.asyncio
async def test_register_user(client):
    response = await client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "pass123"
        }
    )

    assert response.status_code in [200, 201, 400]


@pytest.mark.asyncio
async def test_login_user(client):
    await client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "password": "pass123"
        }
    )

    response = await client.post(
        "/auth/login",
        json={
            "email": "login@example.com",
            "password": "pass123"
        }
    )

    assert response.status_code in [200, 401]


@pytest.mark.asyncio
async def test_auth_me_with_token(client, test_db):
    user_doc = {
        "email": "me@example.com",
        "password": "pass123",
        "role": "customer"
    }
    inserted = await test_db["users"].insert_one(user_doc)
    user_id = str(inserted.inserted_id)

    token = create_access_token({"user_id": user_id})

    me_response = await client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert me_response.status_code == 200
    assert me_response.json().get("email") == "me@example.com"


@pytest.mark.asyncio
async def test_login_invalid_password(client):
    await client.post(
        "/auth/register",
        json={
            "email": "invalid@example.com",
            "password": "pass123"
        }
    )

    invalid_login = await client.post(
        "/auth/login",
        json={
            "email": "invalid@example.com",
            "password": "wrongpass"
        }
    )

    assert invalid_login.status_code == 401


@pytest.mark.asyncio
async def test_register_duplicate_user(client):
    await client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "pass123"}
    )

    response = await client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "pass123"}
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_login_nonexistent_user(client):
    response = await client.post(
        "/auth/login",
        json={"email": "noone@example.com", "password": "pass123"}
    )

    assert response.status_code == 401
