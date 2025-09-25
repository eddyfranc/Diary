from pydantic import BaseModel, EmailStr
from typing import Optional, List

# USER SCHEMAS 
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


# TOKEN SCHEMAS 
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


# NOTE SCHEMAS  
class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# SHARED NOTE SCHEMAS
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
