import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
def test_ops_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/ops/login", json={"email": "ops@example.com", "password": "test"})
        assert response.status_code == 200

@pytest.mark.asyncio
def test_ops_upload():
    # TODO: Implement file upload test
    pass 