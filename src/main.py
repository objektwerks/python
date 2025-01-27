# fastapi
# run: fastapi dev ./src/main.py
# test: curl -v http://localhost:8000/now

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/now")
def now():
  datetime.now().isoformat()