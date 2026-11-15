import httpx

url = "http://127.0.0.1:8000"

body = {
            "user_name": "Seydou Kabore",
            "user_login": "S_kabore",
            "user_email": "skabore2020@gmail.com",
            "user_age": 20,
            "user_height": 190,
            "user_weight": 105 
        }

headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}

try:
    post = httpx.post(
        url+"/user", 
        json=body,
        headers=headers,
        timeout=10
    )
    post.raise_for_status()
    print(f"{body['user_name']} added !")
except httpx.HTTPStatusError as e: 
    if e.response.status_code == 422:
        print("Unprocessable Entity : 422")
    else:
        print(f"Erreur: {e}")

try: 
    get = httpx.get(
        url+"/users", 
        timeout=10
    )
    get.raise_for_status()
    print(get)
    data = get.json()
    print(data)
    print(data['users'][0]['user_name'])
except httpx.HTTPStatusError as e:
    print(f"Erreur: {e}")