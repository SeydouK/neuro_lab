from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 

print("==== Gestion des utilisateurs ====")

app = FastAPI()

class UserIn(BaseModel):
    user_name: str
    user_login: str
    user_email: str
    user_age: int
    user_height: int 
    user_weight: int 

users: list[UserIn] = []

@app.get("/users",status_code=200)
def user():
    return {"status":"ok", "users":users}

@app.get("/user/{user_id}", status_code=200)
def get_user(user_id: int):
    if not 0 <= user_id < len(users): 
        raise HTTPException(status_code=404, 
        detail="This user doesn't exist.")
    return users[user_id]

@app.post("/user", status_code=201)
def add_user(user: UserIn):
    users.append(user)
    return {
        "id": len(users)-1,
        **user.model_dump(),
    }

@app.delete(f"/user/{id}")
def delete_user(user_id:int):
    if not 0 <= user_id <= len(users):
        raise HTTPException(status_code=404, detail="This user doesn't exist.")
    print("This user has been deleted.")


