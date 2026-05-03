"""Tests for the FastAPI endpoints (Phase 4)."""

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_games():
    """GET /api/games should return a non-empty list."""
    resp = client.get("/api/games")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # Each game should have an id and name
    assert "id" in data[0]
    assert "name" in data[0]


def test_get_games_filter_platform():
    """GET /api/games?platform=Mobile returns only mobile games."""
    resp = client.get("/api/games?platform=Mobile")
    assert resp.status_code == 200
    data = resp.json()
    assert all("Mobile" in g["platform"] for g in data)


def test_get_game_by_id():
    """GET /api/games/{id} returns the correct game."""
    resp = client.get("/api/games/minecraft")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == "minecraft"
    assert data["name"] == "Minecraft"


def test_get_game_not_found():
    """GET /api/games/{id} returns 404 for unknown games."""
    resp = client.get("/api/games/notarealgame")
    assert resp.status_code == 404


def test_check_compatibility():
    """POST /api/check returns a valid compatibility result."""
    payload = {
        "game_id": "minecraft",
        "device": {
            "ram_gb": 8,
            "gpu_tier": 3,
            "cpu_tier": 3,
            "storage_gb": 50,
            "os": "Windows 10",
        },
    }
    resp = client.post("/api/check", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["game_id"] == "minecraft"
    assert "verdict" in data
    assert "min_score" in data
    assert "rec_score" in data
    assert "bottleneck" in data


def test_check_compatibility_game_not_found():
    """POST /api/check with unknown game returns 404."""
    payload = {
        "game_id": "nonexistent",
        "device": {
            "ram_gb": 8,
            "gpu_tier": 3,
            "cpu_tier": 3,
            "storage_gb": 50,
            "os": "Windows 10",
        },
    }
    resp = client.post("/api/check", json=payload)
    assert resp.status_code == 404


def test_advisor():
    """POST /api/advisor returns a keyword-matched response."""
    resp = client.post("/api/advisor", json={"message": "How do I upgrade?"})
    assert resp.status_code == 200
    data = resp.json()
    assert "response" in data
    assert "GPU" in data["response"]


def test_advisor_default():
    """POST /api/advisor with unmatched keyword returns default response."""
    resp = client.post("/api/advisor", json={"message": "hello there"})
    assert resp.status_code == 200
    data = resp.json()
    assert "advisor" in data["response"].lower()


def test_contact():
    """POST /api/contact returns received status."""
    resp = client.post(
        "/api/contact",
        json={"name": "Test", "email": "test@test.com", "message": "Hello"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "received"


def test_submit_device():
    """POST /api/submit-device returns saved status."""
    resp = client.post(
        "/api/submit-device",
        json={
            "device_name": "My PC",
            "device": {
                "ram_gb": 16,
                "gpu_tier": 4,
                "cpu_tier": 4,
                "storage_gb": 500,
                "os": "Windows 11",
            },
        },
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "saved"
    assert resp.json()["device_name"] == "My PC"


def test_serve_index():
    """GET / should return index.html."""
    resp = client.get("/")
    assert resp.status_code == 200
