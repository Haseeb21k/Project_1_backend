from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
import models.user
import models.note
from routers import auth, note, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(note.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


