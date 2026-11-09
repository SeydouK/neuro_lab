from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class MessageIn(BaseModel):         
    author: str
    text: str

messages: list[MessageIn] = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/messages", status_code=201)
def add_message(msg: MessageIn):
    messages.append(msg)
    return {"id": len(messages) - 1, **msg.model_dump()}

@app.get("/messages/{msg_id}")      
def get_message(msg_id: int):
    if not 0 <= msg_id < len(messages):
        raise HTTPException(status_code=404, detail="Message not found")
    return messages[msg_id]