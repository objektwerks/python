from datetime import datetime

greeting: str = 'Greetings, Pythonistas!'
print(greeting)

today: datetime = datetime.today()
print('Date: ' + today.strftime('%Y-%m-%d'))
print('Time: ' + today.strftime('%H:%M:%S'))
