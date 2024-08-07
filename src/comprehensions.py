# comprehensions

ints: list[int] = [1, 2, 3]

squares: list[int] = [i * i for i in ints]
print(f'ints {ints} squared {squares}')

evens: list[int] = [i for i in ints if i % 2 == 0]
print(f'even ints {evens}')

odds: list[int] = [i for i in ints if i % 2 != 0]
print(f'odd ints {odds}')

quote: str = "life, uh, finds a way"
vowels: set[str] = {char for char in quote if char in "aeiou"}
print(f'from {quote}, vowels filtered and deduped to {vowels}')
