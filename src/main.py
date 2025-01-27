# fastapi
# run: fastapi dev ./src/main.py
# test: curl -v http://127.0.0.1:8000/now
# test: curl -X POST http://127.0.0.1:8000/command -H "Content-Type: application/json" -d '{"name":"run command"}'

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Command(BaseModel):
  name: str

class Event(BaseModel):
  name: str

app = FastAPI()

@app.get("/now")
def now():
  return f'*** Now: {datetime.now().isoformat()}'

@app.post("/command")
def command(name: str):
  content: str = f'command: {name} to event: {name} run on {datetime.now().isoformat()}'
  return Event(name = content).model_dump_json()