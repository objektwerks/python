# quick sort - O(log n)

def sort(items: list[int]) -> list[int]:
  if len(items) < 2:
    return items
  else:
    pivotItem: int = items[0]
    lesserItems: list[int] = [i for i in items[1:] if i <= pivotItem]
    greaterItems: list[int] = [i for i in items[1:] if i > pivotItem]
    return sort(lesserItems) + [pivotItem] + sort(greaterItems)

ints: list[int] = [3, 2, 1]
print(f'quick sort of ints {ints} sorts to: {sort(ints)}')