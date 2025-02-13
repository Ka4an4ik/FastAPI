from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI


app = FastAPI()

data = {
    "email" : "abc@mail.ru",
    "bio" : None,
    "age" : 10,
}

class UserSchema(BaseModel):
    email: EmailStr | None = Field(default=None)
    bio: str | None 


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)


users = []


@app.post("/users")
def add_user(user: UserAgeSchema):
    users.append(user)
    return {"Ok" : "true", "msg" : "user done"}

@app.get("/users")
def get_users():
    return users