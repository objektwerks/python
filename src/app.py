from datetime import datetime

greeting: str = 'Greetings, Pythonistas!'
print(greeting)

today = datetime.today()
print("Date: " + today.strftime("%x"))
print("Time: " + today.strftime("%X"))
