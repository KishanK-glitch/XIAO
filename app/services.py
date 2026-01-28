from groq import AsyncGroq
from typing import List
from .config import settings
from .models import Message

client = AsyncGroq(api_key=settings.GROQ_API_KEY)

async def generate_response(conversation_history: List[Message]) -> str:
    from .core import get_system_prompt
    
   
    system_prompt = get_system_prompt()
    
  
    messages_payload = [{"role": "system", "content": system_prompt}]
    
   
    for msg in conversation_history:
        messages_payload.append({"role": msg.role, "content": msg.content})
    
    try:
        completion = await client.chat.completions.create(
            messages=messages_payload,
            model=settings.MODEL_NAME,
            temperature=0.7,
            max_tokens=1024,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"System Error: {str(e)}"