# merge sort

def mergesort(items: list[int]):
  if len(items) > 1:
    itemsLen: int = len(items) // 2
    leftItems: list[int] = items[:itemsLen]
    rightItems: list[int] = items[itemsLen:]

    mergesort(leftItems)
    mergesort(rightItems)

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

ints: list[int] = [10, 5, 2, 3]

print(f'merge sort of ints {ints} sorts to: {mergesort(ints)}')
