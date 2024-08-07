# comprehensions

ints: list[int] = [1, 2, 3]

squares: list[int] = [i * i for i in ints]

print(f'ints {ints} squared {squares}')
