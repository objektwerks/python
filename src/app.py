from datetime import datetime

greeting: str = 'Greeting: Greetings, Pythonistas!'
print(greeting)

today: datetime = datetime.today()
print("Date: " + today.strftime('%Y-%m-%d'))
print("Time: " + today.strftime("%X"))
