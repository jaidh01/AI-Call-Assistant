from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

class ChatInput(BaseModel):
    message: str

@app.post("/")
def chat(input: ChatInput):
    user_msg = input.message

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",    # Change the model name according to which model you want to use
            "prompt": user_msg,
            "stream": False 
        }        
    )

    reply = response.json().get("response", "Sorry, I didn't understand that.")
    return {"reply": reply}