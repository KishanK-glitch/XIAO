import json
from pathlib import Path
from .models import ContextData

DATA_PATH = Path("data.json")

def load_context() -> ContextData:
   
    if not DATA_PATH.exists():
        raise FileNotFoundError("data.json not found in root directory.")
    
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        return ContextData(**raw_data)
    except json.JSONDecodeError:
        raise ValueError("CRITICAL: data.json is malformed or empty.")

def get_system_prompt() -> str:
    data = load_context()
    
    prompt = (
        f"You are an AI assistant for {data.user_profile.name}, a {data.user_profile.role} "
        f"at {data.user_profile.college}.\n"
        f"User Interests: {', '.join(data.user_profile.interests)}.\n"
        f"Known Projects: {', '.join(data.projects)}.\n\n"
        f"INSTRUCTIONS: {data.instructions}\n"
        "Keep responses precise, technical, and engineering-focused. "
        "Maintain the persona defined above throughout the conversation."
    )
    return prompt