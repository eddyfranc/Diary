from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class SharedNote(Base):
    __tablename__ = "shared_notes"

    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, ForeignKey("notes.id", ondelete="CASCADE"))
    shared_with_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    note = relationship("Note", back_populates="shared_with")
    shared_with_user = relationship("User", back_populates="shared_notes")
