from fastapi.testclient import TestClient
from api.main import app 

client = TestClient(app)

def test_missing_is_404():
    assert client.get("/messages/99").status_code == 404