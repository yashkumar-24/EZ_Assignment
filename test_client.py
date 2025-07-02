import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
def test_client_signup():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/client/signup", json={"email": "client@example.com", "password": "test"})
        assert response.status_code == 200

@pytest.mark.asyncio
def test_client_login():
    # TODO: Implement client login test
    pass 