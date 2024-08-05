from datetime import datetime

greeting: str = 'Greetings, Pythonistas!'
print(greeting)
print()

today: datetime = datetime.today()
print('Time: ' + today.strftime('%H:%M:%S'))
print('Date: ' + today.strftime('%Y-%m-%d'))

print()
closing: str = 'Code on!'
print(closing)