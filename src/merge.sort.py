# merge sort

def mergesort(items: list[int]):
  if len(items) > 1:
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]

    mergesort(left_half)
    mergesort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            items[k] = left_half[i]
            i += 1
        else:
            items[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        items[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        items[k] = right_half[j]
        j += 1
        k += 1
