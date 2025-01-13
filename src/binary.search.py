# binary search

def binary_search(ints: list[int], item: int) -> int:
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

  return -1

ints: list[int] = [1, 3, 5, 7, 9]

print(f'binary search on ints {ints} for 3 equal index of: {binary_search(ints, 3)}')
print(f'binary search on ints {ints} for 0 equal index of: {binary_search(ints, 0)}')