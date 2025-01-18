# breadth first search

from collections import deque

def traverse(map: dict[int, list[int]], start: int) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)

    for child in map[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return visited

def filter(map: dict[int, list[int]], start: int, filter) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)

    for child in map[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return visited

map: dict[int, list[int]] = {
  1: [2, 3, 4, 5],
  2: [6, 7],
  3: [8],
  4: [9],
  5: [],
  6: [],
  7: [10],
  8: [],
  9: [],
  10: [1]
}

print(f'traverse map {map} in this order: {traverse(map, 1)}')
