# binary search

def indexof(items: list[int], item: int) -> int:
  lowIndex: int = 0
  highIndex: int = len(items) - 1

  while lowIndex <= highIndex:
    mid: int = (lowIndex + highIndex) // 2
    guess: int = items[mid]
    if guess == item:
      return mid
    elif guess > item:
      highIndex = mid - 1
    else:
      lowIndex = mid + 1

  return -1

ints: list[int] = [1, 3, 5, 7, 9]

print(f'binary search on ints {ints} for 3 returns an index of: {indexof(ints, 3)}')
print(f'binary search on ints {ints} for 0 returns an index of: {indexof(ints, 0)}')
