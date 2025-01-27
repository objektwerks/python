# fastapi
# run: fastapi dev ./src/fast.api.py
# test: curl -v http://localhost:8000/now

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/now")
def now():
  datetime.now().isoformat()