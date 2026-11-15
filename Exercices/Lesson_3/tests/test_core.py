from fastapi.testclient import TestClient 
from gestion_utilisateurs import app

client = TestClient(app)

def test_missing_is_404(): 
    assert client.get("/users/99").status_code==404

def test_create_user():
    response = client.post(
        "/user",
        json={
            "user_name": "Seydou Kabore",
            "user_login": "S_kabore",
            "user_email": "skabore2020@gmail.com",
            "user_age": 20,
            "user_height": 190,
            "user_weight": 105 
        }
    )
    assert response.status_code == 201

def test_list_users():
    response = client.get(
        "/users"
    )
    assert response.status_code== 200

def test_get_user():

    response = client.get(
        "/user/0",
    )
    assert response.status_code == 200