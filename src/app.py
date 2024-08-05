from datetime import datetime

greeting: str = 'Greetings, Pythonistas!'
print(greeting)
print()

today: datetime = datetime.today()
print('Date: ' + today.strftime('%Y-%m-%d'))
print('Time: ' + today.strftime('%H:%M:%S'))

print()
closing: str = 'Code on!'
print(closing)