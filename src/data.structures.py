# data structures

from array import array
from collections import namedtuple

ints: list[int] = [1, 2, 3]
print(f'list: {ints}')
print(f'len: {len(ints)}')
print(f'type: {type(ints)}')

bag: list[str | int] = ['a', 1, 'b', 2, 'c', 3]
print(f'bag: {bag}')
print(f'len: {len(bag)}')
print(f'type: {type(bag)}')

strings: tuple[str, str, str] = ('a', 'b', 'c')
print(f'tuple: {strings}')
print(f'type: {type(strings)}')

point: tuple[float, float] = namedtuple('point', 'x y')
point1 = point(1.0, 2.0)
point2 = point(3.0, 4.0)
print(f'point 1: {point1.x}/{point1.y}')
print(f'point 2: {point2.x}/{point2.y}')
print(f'type: {type(point)}')

floats: set[float] = {1.1, 2.2, 3.3, 1.1, 2.2, 3.3}
print(f'set: {floats}')
print(f'len: {len(floats)}')
print(f'type: {type(floats)}')

pairs: dict[int, str] = {1: 'a', 2: 'b', 3: 'c'}
print(f'dict: {pairs}')
print(f'len: {len(pairs)}')
print(f'type: {type(pairs)}')

numbers: array[int] = array('i', [1, 2, 3])
print(f'array: {numbers}')
print(f'len: {len(numbers)}')
print(f'type: {type(numbers)}')

animals = ["ferret", "vole", "dog", "gecko"]
print(f'sorted animals to {sorted(animals)}')
print(f'sorted animals by len to {sorted(animals, key=len)}')
