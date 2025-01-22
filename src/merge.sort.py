# merge sort - O(log n)

def sort(items: list[int]) -> None:
  if len(items) > 1:
    itemsLen: int = len(items) // 2
    leftItems: list[int] = items[:itemsLen]
    rightItems: list[int] = items[itemsLen:]

    sort(leftItems)
    sort(rightItems)

    i: int = 0
    j: int = 0
    k: int = 0

    while i < len(leftItems) and j < len(rightItems):
      if leftItems[i] < rightItems[j]:
        items[k] = leftItems[i]
        i += 1
      else:
        items[k] = rightItems[j]
        j += 1
      k += 1

    while i < len(leftItems):
      items[k] = leftItems[i]
      i += 1
      k += 1

    while j < len(rightItems):
      items[k] = rightItems[j]
      j += 1
      k += 1

ints: list[int] = [3, 2, 1]
sort(ints)
print(f'merge sort of ints {[3, 2, 1]} sorts in-place to: {ints}')