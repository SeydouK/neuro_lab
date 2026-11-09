import httpx 

# Exercice 1

while True: 
    pokemon = input("Entrez le pokemon a chercher: ")
    try :
        r = httpx.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}", timeout=10)
        r.raise_for_status()
        data = r.json()

        print(data['name'], data['weight'], data['abilities'])
        break
    except httpx.HTTPStatusError as e:
        print("Erreur : e")
    


# Exercice 2 
users = httpx.get("https://jsonplaceholder.typicode.com/users", timeout=10)
while True: 
    try: 
        user = int(input("Enter the user's ID: "))
        r = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user}", timeout=10)
        print(r.raise_for_status())
        data = r.json()

        #print(data.keys())
        print(f"Number of users: {len(users.json())}")
        print(f"Name: {data['name']}, \n Email: {data['email']}, \n City: {data['address']}, \n {data['company']}")
        break
    except httpx.HTTPStatusError as e:
        print(f"Erreur : {e}")

# Exercice 3 
url = "https://jsonplaceholder.typicode.com/posts"
response = httpx.get(
    url, 
    params={'userId':1},
    timeout=10
)
posts = response.json()[:5]

for i in posts:
    print(i)

# Ecercice 4 
url = "https://api.github.com/search/repositories"

params = {
    "q":"python", 
    "sort":"stars",
    "per_page":10

}

response = httpx.get(
    url, 
    params=params,
    timeout=10
)

libraries = response.json()

for library in libraries["items"]: 
    print(library['name'])

# Exercice 5
url = "https://jsonplaceholder.typicode.com/posts"
response_post = httpx.post(
    url, 
    json={
        "title":"Learning HTTPX", 
        "body": "My first POST request",
        "userId":1
    }, 
    timeout=10
)

response_get = httpx.get(
    url, 
    params={'userId':1},
    timeout=10
)

post = response_get.json()
print(post)

# Exercice 6 
import requests 

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Authorization": "Bearer test-token",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
response = requests.post(url, headers=headers, json={"name":"John"})
response = requests.put(url, headers=headers, json={"name":"David"})
response = requests.delete(url, headers=headers)
print("Status Code:", response.status_code)
print("Headers received by the server:")
print(response.json())

# FastAPI 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 

app = FastApi()

class MessageIn(BaseModel):
    author: str
    text: str 

messages: list[MessageIn] = []

@app.get("/health")
def health(): 
    return {"status":"ok"}

@app.post("/messages", status_code=201)
def add_message(msg: MessageIn):
    messages.append(msg)
    return {"id":len(messages)-1, **msg.model_dump()}

@app.get("/messages/{msg_id}")
def get_message(msg_id: int):
    if not 0 <= msg_id <len(messages):
        raise HTTPException(status_code=404, detail="Message not found")
    return messages[msg_id]

