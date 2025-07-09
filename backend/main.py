from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.chat_logic import query_huggingface
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount frontend
frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")

# ✅ This route MUST be defined BEFORE mounting "/"
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    response = query_huggingface(user_input)
    return {"response": response}
