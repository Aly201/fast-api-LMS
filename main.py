from fastapi import FastAPI , Path,Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI LMS",
    description="This is a simple LMS API",
    version="1.0.0",
    contact={
        "name": "Aly Yasser",
        "email": "ali.yasser.11@gmail.com",
    },
)

class User(BaseModel):
    name: str
    email: str

users=[]
@app.get("/users")
def read_users():
    return users


@app.post("/users")
def create_user(user: User):
    users.append(user)
    return "success"

@app.get("/users/{id}")
def read_user(id: int = Path(..., description="The ID of the user to retrieve"),
              isactive: Optional[bool] = Query(None, description="Whether the user is active"),
              email:str = Query(..., description="The email of the user")
              ):
    return {"id":users[id],"isactive":isactive,"email":users[id].email}



# if __name__ == "__main__":
#     app.run()