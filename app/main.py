from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import ChatRequest
from .services import generate_response

app = FastAPI(title="XIAO Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    response = await generate_response(request.messages)
    return {"response": response}

@app.get("/health")
def health_check():
    return {"status": "active", "system": "XIAO"}