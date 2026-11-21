import httpx 

r = httpx.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=100", timeout=10)

for result in r.json()['results']:
    print(result['name'])
    print(" ")
print(r)
print(r.json().items())