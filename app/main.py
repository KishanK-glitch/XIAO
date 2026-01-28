from fastapi import FastAPI
from .models import ChatRequest
from .services import generate_response

app = FastAPI(title="XIAO Backend")

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # Pass the full list of messages to the service
    response = await generate_response(request.messages)
    return {"response": response}

@app.get("/health")
def health_check():
    return {"status": "active", "system": "XIAO"}
