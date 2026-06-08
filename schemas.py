from pydantic import BaseModel, EmailStr
from typing import Optional

# ── User ────────────────────────────────────────────────────
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str

# ── Task ────────────────────────────────────────────────────
class TaskCreate(BaseModel):
    title: str
    description: str = ""
    status: str = "pending"
    priority: str = "medium"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None

class TaskResponse(TaskCreate):
    id: int
    owner_id: int
    model_config = {"from_attributes": True}