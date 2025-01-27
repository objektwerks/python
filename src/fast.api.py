# fastapi

from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/now")
def now():
  datetime.now().isoformat()