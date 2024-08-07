# comprehensions

ints: list[int] = [1, 2, 3]

squares: list[int] = [i * i for i in ints]
print(f'ints {ints} squared {squares}')

evens: list[int] = [i for i in ints if i / 2 == 0]
print(f'even ints {evens}')

