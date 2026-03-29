import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.db import mongo_client as db_module
from app.core.config import settings

MONGO_URL = settings.MONGO_URI
TEST_DB_NAME = "bookstore_test"


@pytest_asyncio.fixture(scope="function")
async def mongo_client():
    client = AsyncIOMotorClient(MONGO_URL)
    yield client
    client.close()


@pytest_asyncio.fixture
async def test_db(mongo_client):
    db = mongo_client[TEST_DB_NAME]
    yield db
    await db.client.drop_database(TEST_DB_NAME)


@pytest_asyncio.fixture
async def client(test_db):
    db_module.db = test_db
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as c:
        yield c
    
    db_module.db = None


@pytest_asyncio.fixture(autouse=True)
async def clean_db(test_db):
    await test_db["users"].delete_many({})
    await test_db["books"].delete_many({})
    await test_db["orders"].delete_many({})
    
    yield
    
    await test_db["users"].delete_many({})
    await test_db["books"].delete_many({})
    await test_db["orders"].delete_many({})
