import pytest


@pytest.mark.asyncio
async def test_get_books(client):
    response = await client.get("/books/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
