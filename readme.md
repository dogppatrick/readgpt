how to get gpt_session_token
login https://chat.openai.com/
cookies-> __Secure-next-auth.session-token


python -m gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --timeout 1200