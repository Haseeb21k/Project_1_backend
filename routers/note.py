from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.note import NoteCreate, NoteOut, NoteUpdate
from models.note import Note
from models.user import User
from utils.auth import get_current_user

router = APIRouter(prefix="/note", tags=["note"])

@router.post("/", response_model=NoteOut)
def create_notes(note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_note = Note(title=note.title, content=note.content, owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=list[NoteOut])
def get_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Note).filter(Note.owner_id == current_user.id).all()

@router.get("/{id}", response_model=NoteOut)
def get_note(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == id, Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code= 404, detail="Note not found")
    return note

@router.put("/{id}", response_model=NoteOut)
def update_note(id: int, note: NoteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note_db = db.query(Note).filter(Note.id == id, Note.owner_id == current_user.id).first()
    if not note_db:
        raise HTTPException(status_code= 404, detail="Note not found")
    
    if note.title:
        note_db.title = note.title
    if note.content:
        note_db.content = note.content
    db.commit()
    db.refresh(note_db)
    return note_db

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id, Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code= 404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}