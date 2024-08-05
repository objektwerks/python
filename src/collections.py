# collections

ints: list[int] = [1, 2, 3]
print(f'list: {ints}')
print(f'len: {len(ints)}')
print(f'type: {type(ints)}')

bag: list[str | int] = ['a', 1, 'b', 2, 'c', 3]
print(f'bag: {bag}')
print(f'len: {len(bag)}')
print(f'type: {type(bag)}')

strings: tuple[str, str, str] = ('a', 'b', 'c')
print(f'tuple: {tuple}')
print(f'type: {type(strings)}')
