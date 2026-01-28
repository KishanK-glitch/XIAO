from pydantic import BaseModel
from typing import List, Optional, Dict

class UserProfile(BaseModel):
    name: str
    role: str
    college: Optional[str] = None
    interests: List[str]

class ContextData(BaseModel):
    user_profile: UserProfile
    instructions: str
    projects: List[str]


class Message(BaseModel):
    role: str  
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]