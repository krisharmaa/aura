from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.chat_logic import query_huggingface

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Aura backend live"}

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message", "")
        if not user_input:
            return {"response": "Please enter a message."}

        response = query_huggingface(user_input)
        return {"response": response}
    except Exception as e:
        print("Error in /chat endpoint:", e)
        return {"response": "Internal server error. Please try again later."}
