from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ This handles browser GET requests to root
@app.get("/")
def home():
    return {"message": "SiteWise Bot is running. POST to /chat."}

# ✅ This handles chat POST requests
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    question = body.get("question")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )

    answer = response['choices'][0]['message']['content']
    return JSONResponse(content={"answer": answer})
