# dijkstra's algo - O((v + e) log v)

from dataclasses import dataclass
import heapq
from typing import Optional

graph: dict[str, dict[str, float]] = {
  's': {'a':8, 'b':4},
  'a': {'b':4},
  'b': {'a':3, 'c':2, 'd':5},
  'c': {'d':2},
  'd': {}
}

@dataclass
class Node:
  x: int = 0
  y: int = 0
  distance: float = float('inf')
  parent: Optional[str] = None
  finished: bool = False

def findShortestPaths(graph: dict[str, dict[str, float]], source: str) -> dict[str, float]:
  nodes: dict[str, Node] = {node: Node(0, 0) for node in graph}
  nodes[source].distance = 0
  queue: list[tuple[float, str]] = [ (0, source) ]

  while queue:
    distance, node = heapq.heappop(queue)
    if nodes[node].finished:
      continue
    nodes[node].finished = True

    for neighbor, weight in graph[node].items():
      if nodes[neighbor].finished:
        continue
      newDistance = distance + weight
      if newDistance < nodes[neighbor].distance:
        nodes[neighbor].distance = newDistance
        nodes[neighbor].parent = node
        heapq.heappush(queue, (newDistance, neighbor))

  shortestPaths: dict[str, float] = {node: nodes[node].distance for node in nodes}

  return shortestPaths

print(f'graph {graph}')
print(f'find shortest paths: {findShortestPaths(graph, "s")}')