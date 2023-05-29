import requests
from fastapi import APIRouter, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from router import gpt_summary

app = FastAPI()

class Item(BaseModel):
    url: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 您的前端網域
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(gpt_summary)