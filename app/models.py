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

# NEW: Structure for a single message
class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

# UPDATE: Request now accepts a list of messages
class ChatRequest(BaseModel):
    messages: List[Message]