from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # Relationships
    owner = relationship("User", back_populates="notes")
    shared_with = relationship("SharedNote", back_populates="note", cascade="all, delete-orphan")


