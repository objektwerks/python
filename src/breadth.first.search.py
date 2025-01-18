# breadth first search

from collections import deque

def breadthFirstSearch(map: dict[int, list[int]], start: int) -> list[int]:
  queue: deque[int] = deque([start])
  visited: list[int] = []

  while queue:
    node: int = queue.popleft()
    visited.append(node)

    for child in map[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return visited

map = {
    1: [2, 3, 4, 5],
    2: [6, 7],
    3: [8],
    4: [9]
}
