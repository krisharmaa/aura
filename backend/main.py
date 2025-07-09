from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.chat_logic import query_huggingface 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "aura backend live"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    response = query_huggingface(user_input)

    return {"response": response}