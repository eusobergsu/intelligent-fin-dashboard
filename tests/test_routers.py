from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_market_summary():
    r = client.get("/market/summary")
    assert r.status_code == 200
    data = r.json()
    assert "data" in data and isinstance(data["data"], list)

def test_crypto_summary():
    r = client.get("/crypto/summary")
    assert r.status_code == 200
    data = r.json()
    assert "data" in data and isinstance(data["data"], list)
