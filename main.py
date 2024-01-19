from typing import List, Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username : str
    email: str
    is_active : bool = True
    bio : Optional[str] = None


users = []

@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/user')
async def create_user(user : User):
    users.append(user)
    return {'message':'Create successfully'}

@app.get('/user/{id}')
async def get_user(id : int = Path(...,description="Id not found", gt=2)):
    return users[id]