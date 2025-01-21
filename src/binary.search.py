# binary search - O(log n)

def indexof(items: list[int], item: int) -> int:
  lowIndex: int = 0
  highIndex: int = len(items) - 1

  targetItemIndex: int = -1

  while lowIndex <= highIndex:
    midIndex: int = (lowIndex + highIndex) // 2
    midIndexItem: int = items[midIndex]
    if midIndexItem == item:
      targetItemIndex = midIndex
      break
    elif midIndexItem > item:
      highIndex = midIndex - 1
    else:
      lowIndex = midIndex + 1

  return targetItemIndex

ints: list[int] = [1, 3, 5, 7, 9]
print(f'binary search on ints {ints} for indexof 3 returns an indexof: {indexof(ints, 3)}')
print(f'binary search on ints {ints} for indexof 0 returns an indexof: {indexof(ints, 0)}')