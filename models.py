from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    tasks           = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    description = Column(String, default="")
    status      = Column(String, default="pending")    # pending | in-progress | done
    priority    = Column(String, default="medium")     # low | medium | high
    owner_id    = Column(Integer, ForeignKey("users.id"), nullable=False)
    owner       = relationship("User", back_populates="tasks")  