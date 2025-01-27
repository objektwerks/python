# fastapi
# run: fastapi dev ./src/main.py
# test: curl -v http://127.0.0.1:8000/now
# test: curl -X POST http://127.0.0.1:8000/command -H "Content-Type: application/json" -d '{"name":"command"}'

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/now")
def now():
  return f'*** Now: {datetime.now().isoformat()}'