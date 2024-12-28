from fastapi import APIRouter , Path,Query
from typing import Optional
from pydantic import BaseModel

router=APIRouter()


class User(BaseModel):
    name: str
    email: str

users=[]
@router.get("/users")
def read_users():
    return users


@router.post("/users")
def create_user(user: User):
    users.append(user)
    return "success"

@router.get("/users/{id}")
def read_user(id: int ):
    return {"users":users[id] }