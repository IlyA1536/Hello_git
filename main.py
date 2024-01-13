from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 

app = FastAPI()

class User (BaseModel):
    id: int
    username: str
    email: str

users = [
    User (id=1, username="user1", email="user1@gmail.com"),
    User (id=2, username="user2", email="user2@gmail.com"),
]

@app.get("/users/(user_id)")
def read_user(user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return User