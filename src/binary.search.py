# binary search

from typing import List

def binary_search(ints: List[int], item: int):
    low = 0
    high = len(ints) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = ints[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

ints: List[int] = [1, 3, 5, 7, 9]

print(f'binary search on ints {ints} for 3 == {binary_search(ints, 3)}')

print(binary_search(ints, -1)) # => None