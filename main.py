import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    url: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 您的前端網域
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/")
async def process_url(request: dict):
    payload = request.get("data", {})
    processed_data = f"Processing URL: {payload.get('url')}"
    print(f'{request}')
    return {"result": processed_data}

def web_context_extract(url):
    pass

def summary_result():
    pass