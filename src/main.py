# fastapi
# run: fastapi dev ./src/main.py
# test: curl -v http://127.0.0.1:8000/now

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/now")
def now():
  return f'*** Current date and time: {datetime.now().isoformat()}'