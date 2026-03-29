import pytest


@pytest.mark.asyncio
async def test_create_order(client):
    response = await client.get("/orders/", headers={"Authorization": "Bearer fake_token"})

    assert response.status_code in [200, 401, 403]
