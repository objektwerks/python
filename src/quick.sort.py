# quick sort

def quicksort(items: list[int]) -> list[int]:
  if len(items) < 2:
    return items
  else:
    pivot = items[0]
    less = [i for i in items[1:] if i <= pivot]
    greater = [i for i in items[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

ints: list[int] = [10, 5, 2, 3]

print(f'quick sort of ints {ints} sorts to: {quicksort(ints)}')
