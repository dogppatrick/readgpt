import requests
from fastapi import APIRouter, FastAPI, Response
from text_extract import sf_article_extract
from summary import summarize_article_chatgpt

gpt_summary = APIRouter(prefix='/gpt_summary')

@gpt_summary.post("/")
async def process_url(request: dict):
    payload = request.get("data", {})
    target_url = payload.get('url')
    processed_data = f"Processing URL: {target_url}"
    content_text = web_context_extract(target_url)
    summary = summarize_article_chatgpt(content_text)
 
    return {"result": processed_data, "summary":summary}

def web_context_extract(url):
    resp = requests.get(url)
    resp_text = resp.text
    content_text = sf_article_extract(resp_text)
    return content_text

# url = 'https://www.stockfeel.com.tw/%e8%b2%a1%e7%b6%93%e6%96%b0%e8%81%9e-%e6%96%b0%e8%81%9e%e4%ba%8b%e4%bb%b6-%e5%9c%8b%e9%9a%9b%e5%a4%a7%e4%ba%8b/'
# target_url = url
# processed_data = f"Processing URL: {target_url}"
# content_text = web_context_extract(target_url)
# summary = summarize_article_chatgpt(content_text)