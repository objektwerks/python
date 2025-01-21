# quick sort - O(log n)

def quickSort(items: list[int]) -> list[int]:
  if len(items) < 2:
    return items
  else:
    pivotItem: int = items[0]
    lesserItems: list[int] = [i for i in items[1:] if i <= pivotItem]
    greaterItems: list[int] = [i for i in items[1:] if i > pivotItem]
    return quickSort(lesserItems) + [pivotItem] + quickSort(greaterItems)

ints: list[int] = [10, 5, 2, 3]
print(f'quick sort of ints {ints} sorts to: {quickSort(ints)}')