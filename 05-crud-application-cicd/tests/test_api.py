import pytest
from app import create_app

@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.sqlite")})
    return app.test_client()

def test_crud_lifecycle(client):
    made = client.post("/items", json={"name": "Notebook"})
    assert made.status_code == 201
    item_id = made.json["id"]
    assert client.get("/items").json == [{"id": item_id, "name": "Notebook"}]
    assert client.put(f"/items/{item_id}", json={"name": "Journal"}).json["name"] == "Journal"
    assert client.delete(f"/items/{item_id}").status_code == 204
    assert client.get("/items").json == []

def test_name_required(client):
    assert client.post("/items", json={}).status_code == 400
