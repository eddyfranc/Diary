from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import database, models
from app.routes.auth import get_current_user  

router = APIRouter( prefix="/shared-notes", tags=["Shared Notes"])

@router.post("/")
def share_note(note_id: int, shared_with_user_id: int, db: Session = Depends(database.get_db), current_user: models.user.User = Depends(get_current_user)):
    note = db.query(models.note.Note).filter(models.note.Note.id == note_id, models.note.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found or not yours")

    shared_entry = models.shared_note.SharedNote(
        note_id=note_id,
        shared_with_user_id=shared_with_user_id
    )
    db.add(shared_entry)
    db.commit()
    db.refresh(shared_entry)
    return shared_entry

@router.get("/")
def get_shared_notes(db: Session = Depends(database.get_db), current_user: models.user.User = Depends(get_current_user)):
    shared_notes = db.query(models.shared_note.SharedNote).filter(
        models.shared_note.SharedNote.shared_with_user_id == current_user.id
    ).all()
    return shared_notes
