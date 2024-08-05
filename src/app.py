from datetime import datetime

greeting: str = 'Greetings, Pythonistas!'
print(greeting)

today = datetime.now

print(today.strftime("%x"))
print(today.strftime("%X"))
