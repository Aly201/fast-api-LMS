from fastapi import FastAPI , Path,Query
from typing import Optional
from pydantic import BaseModel
from api.users import router


app = FastAPI(
    title="FastAPI LMS",
    description="This is a simple LMS API",
    version="1.0.0",
    contact={
        "name": "Aly Yasser",
        "email": "ali.yasser.11@gmail.com",
    },
)

app.include_router(router)





# if __name__ == "__main__":
#     app.run()