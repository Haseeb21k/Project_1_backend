from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title: str | None = None
    content: str | None = None

class NoteOut(NoteBase):
    id: int

    class Config:
        orm_mode = True