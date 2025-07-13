from pydantic import BaseModel, EmailStr

class userCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class userout(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        orm_mode = True