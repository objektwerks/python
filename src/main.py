# fastapi
# run: fastapi dev ./src/main.py
# test: curl -v http://127.0.0.1:8000/now
# test: curl -X POST http://127.0.0.1:8000/command -H "Content-Type: application/json" -d '{"name":"execute command"}'

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
def command(command: Command):
  # Demonstrates a command handler, with pattern matching, could work here with commands in and events out.
  content: str = f'command: {command.name} >>> event: command executed at {datetime.now().isoformat()}'
  return Event(name = content).model_dump_json()