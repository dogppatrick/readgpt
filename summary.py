import openai

from chatgptv2 import ChatGPT
from open_ai_key import gpt_session_token, key

gpt = ChatGPT(gpt_session_token)

def summarize_article_openai(article):
    def open_ai_summary(text):
        openai.api_key = key
        prompt = f"Generate a summary of the following article with tradition chinese:\n\n{text}" 
        response = openai.Completion.create(
            engine='text-curie-001',
            prompt=prompt,
            max_tokens=max_tokens_per_request,
            temperature=0.3,
            top_p=0.95,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None,
            n=1,
            return_prompt=False
        )
        summary = response.choices[0].text.strip()
        return summary

    if len(article) > 8000:
        article = article[:8000]
    max_tokens_per_request = 2000
    article_chunks = [article[i:i + max_tokens_per_request] for i in range(0, len(article), max_tokens_per_request)]

    summaries = []
    i = 0
    for chunk in article_chunks:
        summary = open_ai_summary(chunk)
        print(f'{i}|{summary}')
        i+=1
        summaries.append(summary)

    final_summary = ' '.join(summaries)
    
    if len(article_chunks)>1:
        return open_ai_summary(final_summary)
    return final_summary

def summarize_article_chatgpt(article):
    def chatgpt_summary(text):
        prompt = f"Generate a summary of with tradition chinese in with shorter content:\n\n{text}" 
        result = gpt.send_message(prompt)
        return result

    if len(article) > 2000:
        article = article[:2000]
    max_tokens_per_request = 1000
    article_chunks = [article[i:i + max_tokens_per_request] for i in range(0, len(article), max_tokens_per_request)]

    summaries = []
    i = 0
    for chunk in article_chunks:
        summary = chatgpt_summary(chunk)
        print(f'{i}|{summary}')
        i+=1
        summaries.append(summary)

    final_summary = ' '.join(summaries)
    
    if len(article_chunks)>1:
        return chatgpt_summary(final_summary)
    return final_summary