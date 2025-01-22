# selections sort x - O(n^2)

def sort(items: list[int]) -> None:
  for i in range(len(items) - 1):
    lowestItemIndex = i

    for j in range(i + 1, len(items)):
      if items[j] < items[lowestItemIndex]:
        lowestItemIndex = j

    if lowestItemIndex != i:
      items[i], items[lowestItemIndex] = items[lowestItemIndex], items[i]
    
  return None

ints: list[int] = [3, 2, 1]
sort(ints)
print(f'selection sort on ints {[3, 2, 1]} sorts in-place to: {ints}')