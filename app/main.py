from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageRequest(BaseModel):
    username: str

@app.get("/")
async def greet():
    return {"reply": f"Hello, I'm your friendly Teams bot! 😊"}

@app.post("/api/message")
async def handle_message(msg: MessageRequest):
    return {"reply": f"Hello {msg.username}, I'm your friendly Teams bot! 😊"}
