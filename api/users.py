from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username : str
    email: str
    is_active : bool = True
    bio : Optional[str] = None


users = []

@router.get('/users', response_model=List[User])
async def get_users():
    return users


@router.post('/user')
async def create_user(user : User):
    users.append(user)
    return {'message':'Create successfully'}

@router.get('/user/{id}')
async def get_user(id : int):
    return users[id]