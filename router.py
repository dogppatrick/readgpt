import requests
from fastapi import APIRouter, FastAPI, Response
from text_extract import sf_article_extract
from summary import summarize_article_chatgpt

gpt_summary = APIRouter(prefix='/gpt_summary')

cache = dict()

@gpt_summary.post("/")
async def process_url(request: dict):
    payload = request.get("data", {})
    target_url = payload.get('url')
    if cache.get(target_url):
        return cache.get(target_url)
    else:
        print(f'no cache exists')
    processed_data = f"Processing URL: {target_url}"
    content_text = web_context_extract(target_url)
    content_text = content_text[:500]
    summary = summarize_article_chatgpt(content_text)
    response = {"result": processed_data, "summary":summary}
    cache[target_url] = response
    return response

def web_context_extract(url):
    resp = requests.get(url)
    resp_text = resp.text
    content_text = sf_article_extract(resp_text)
    return content_text