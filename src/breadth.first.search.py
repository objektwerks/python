# breadth first search

from collections import deque

def breadthFirstSearch(map: dict[int, list[int]], start: int):
  queue = deque([start])
  visited = []

  while queue:
    node = queue.popleft()
    visited.append(node)

    for child in map[node]:
      if child not in visited and child not in queue:
        queue.append(child)

  return visited
