import pytest
from fastapi.testclient import TestClient

from chathub.api import create_app
from chathub.store import MessageStore


@pytest.fixture
def client(tmp_path):
    return TestClient(create_app(MessageStore(tmp_path / "messages.json")))


def post(client, author="vedal", text="hello", **kwargs):
    return client.post("/messages", json={"author": author, "text": text}, **kwargs)


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_create_returns_201_and_the_message(client):
    r = post(client)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["author"] == "vedal"
    assert body["text"] == "hello"


def test_get_message(client):
    post(client, text="bonjour")
    assert client.get("/messages/1").json()["text"] == "bonjour"


def test_get_unknown_is_404(client):
    assert client.get("/messages/99").status_code == 404


def test_missing_field_is_422(client):
    assert client.post("/messages", json={"author": "x"}).status_code == 422


def test_list_with_limit(client):
    for i in range(3):
        post(client, text=f"msg {i}")
    assert len(client.get("/messages").json()) == 3
    last_two = client.get("/messages", params={"limit": 2}).json()
    assert [m["text"] for m in last_two] == ["msg 1", "msg 2"]


def test_delete(client):
    post(client)
    r = client.delete("/messages/1")
    assert r.status_code == 200
    assert r.json() == {"deleted": 1}
    assert client.get("/messages/1").status_code == 404


def test_delete_unknown_is_404(client):
    assert client.delete("/messages/99").status_code == 404


def test_stats(client):
    post(client, text="hello world")
    post(client, text="hello")
    data = client.get("/stats", params={"top": 1}).json()
    assert data["total"] == 2
    assert data["top_words"] == [["hello", 2]]
    assert data["by_author"] == {"vedal": 2}


def test_api_key_protects_writes_only():
    client = TestClient(create_app(MessageStore(), api_key="secret"))
    assert post(client).status_code == 401
    assert post(client, headers={"X-API-Key": "wrong"}).status_code == 401
    assert post(client, headers={"X-API-Key": "secret"}).status_code == 201
    assert client.get("/messages").status_code == 200
    assert client.delete("/messages/1").status_code == 401
    assert client.delete("/messages/1", headers={"X-API-Key": "secret"}).status_code == 200
