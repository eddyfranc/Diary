from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database
from app.routes.auth import get_current_user

router = APIRouter( prefix="/notes", tags=["Notes"])

# Create Note
@router.post("/", response_model=schemas.NoteResponse)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    new_note = models.Note(**note.dict(), owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


# Get My Notes 
@router.get("/", response_model=List[schemas.NoteResponse])
def get_notes(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    return db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()


# Get Single Note (owner or shared user) 
@router.get("/{id}", response_model=schemas.NoteResponse)
def get_note(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    # if not owner, check if note is shared with current user
    if note.owner_id != current_user.id:
        shared = (
            db.query(models.SharedNote)
            .filter(
                models.SharedNote.note_id == id,
                models.SharedNote.shared_with_user_id == current_user.id,
            )
            .first()
        )
        if not shared:
            raise HTTPException(status_code=403, detail="Not authorized to view this note")

    return note


# Owner Update Note
@router.put("/{id}", response_model=schemas.NoteResponse)
def update_note(
    id: int,
    note_data: schemas.NoteCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    note = db.query(models.Note).filter(models.Note.id == id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by you")

    note.title = note_data.title
    note.content = note_data.content
    db.commit()
    db.refresh(note)
    return note


# Owner Delete Note
@router.delete("/{id}")
def delete_note(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    note = db.query(models.Note).filter(models.Note.id == id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by you")

    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}


# Share Note
@router.post("/{id}/share", response_model=schemas.SharedNoteResponse)
def share_note(
    id: int,
    shared_data: schemas.SharedNoteCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    note = db.query(models.Note).filter(models.Note.id == id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by you")

    # Ensure target user exists
    target_user = db.query(models.User).filter(models.User.id == shared_data.shared_with_user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Target user not found")

    shared_note = models.SharedNote(note_id=id, shared_with_user_id=shared_data.shared_with_user_id)
    db.add(shared_note)
    db.commit()
    db.refresh(shared_note)
    return shared_note


# Revoke Sharing for only owner
@router.delete("/{id}/share/{user_id}")
def revoke_share(
    id: int,
    user_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    note = db.query(models.Note).filter(models.Note.id == id, models.Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found or not owned by you")

    shared = (
        db.query(models.SharedNote)
        .filter(models.SharedNote.note_id == id, models.SharedNote.shared_with_user_id == user_id)
        .first()
    )
    if not shared:
        raise HTTPException(status_code=404, detail="Sharing not found")

    db.delete(shared)
    db.commit()
    return {"message": f"Sharing revoked for user {user_id}"}


# Get Notes Shared With Me 
@router.get("/shared-with-me", response_model=List[schemas.NoteResponse])
def get_shared_notes(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    shared_notes = (
        db.query(models.Note)
        .join(models.SharedNote)
        .filter(models.SharedNote.shared_with_user_id == current_user.id)
        .all()
    )
    return shared_notes
