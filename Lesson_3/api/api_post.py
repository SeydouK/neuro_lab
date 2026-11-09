import os
import httpx 
 
key = os.environ["API_KEY"]
httpx.post(url, json={"text": "hi"}, headers={"Authorization": f"Bearer {key}"}, timeout=10)