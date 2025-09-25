from pydantic import BaseModel

class SharedNoteBase(BaseModel):
    note_id: int
    shared_with_user_id: int

class SharedNoteCreate(SharedNoteBase):
    pass

class SharedNoteResponse(BaseModel):
    id: int
    note_id: int
    shared_with_user_id: int

    class Config:
        from_attributes = True
