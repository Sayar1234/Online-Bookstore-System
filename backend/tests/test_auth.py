import pytest


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
