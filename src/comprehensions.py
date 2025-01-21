# comprehensions

import random

ints: list[int] = [1, 2, 3]

squares: list[int] = [i * i for i in ints]
print(f'ints {ints} squared {squares}')

evens: list[int] = [i for i in ints if i % 2 == 0]
print(f'even ints {evens}')

odds: list[int] = [i for i in ints if i % 2 != 0]
print(f'odd ints {odds}')

quote: str = "When life throws you a few lemons, make lemonade!"
vowels: set[str] = {char for char in quote if char in "aeiou"}
print(f'from \'{quote}\', with vowels filtered and deduped to {vowels}')

pairs: dict[int, int] = {1: 1, 2: 2, 3: 3}
squared: dict[int, int] = {value: value * value for value in pairs}
print(f'pairs {pairs} squared {squared}')

def getTemps():
  return random.randrange(70, 100)

temps: list[int] = [temp for _ in range(10) if (temp := getTemps()) >= 85]
print(f'for temps [70 - 100] >= 85 {temps}')

generator: int = sum(i for i in range(1_000_000))
print(f'generator sum range(1_000_000) to {generator} ')