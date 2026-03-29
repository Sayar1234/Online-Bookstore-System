import pytest


@pytest.mark.asyncio
async def test_get_users(client):
    response = await client.get("/users/", headers={"Authorization": "Bearer fake_token"})

    assert response.status_code in [200, 401, 403]
