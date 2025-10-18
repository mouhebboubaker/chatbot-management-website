from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User ,updatedUser
 

app=FastAPI()

db:List[User]=[
    User(id=uuid4(), first_name="John", last_name="Doe",gender=Gender.female, roles=[Role.admin, Role.user]),
    User(id=uuid4(), first_name="alex", last_name="jones",gender=Gender.female, roles=[Role.admin, Role.user])
]   

@app.get("/")
def root():
    return {"hello":"worldd"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user:User):
    print(user)
    db.append(user)
    return {"id":user.id}
    
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
        
    )
    

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id,updatedUser:updatedUser):
    print(user_id)
    print(f"the updated one is {updatedUser.first_name}")
    return {"response": "hello" }