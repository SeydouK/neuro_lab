from typing import Any


import httpx 

r = httpx.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
r.raise_for_status()
data = r.json()

print(list[Any](data.keys()))
print(
    data['id'],
    data['name'],
    data['height']
)
