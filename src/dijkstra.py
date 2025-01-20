# dijkstra's algo

from dataclasses import dataclass
import heapq

graph: dict[str, dict[str, int]] = {
  's': {'a':8, 'b':4},
  'a': {'b':4},
  'b': {'a':3, 'c':2, 'd':5},
  'c': {'d':2},
  'd': {}
}

@dataclass(frozen=True)
class Node:
  x: int = 0
  y: int = 0
  distance: float = float('inf')
  parent = None
  finished: bool = False

def dijkstra(graph: dict[str, dict[str, int]], source: Node):
  nodes = {}
  for node in graph:
    nodes[node] = Node()
  nodes[source].distance = 0

  queue: list[tuple[int, Node]] = [ (0, source) ]

  while queue:
      distance = heapq.heappop(queue)
      node = heapq.heappop(queue)

      if nodes[node].finished:
          continue
      nodes[node].finished=True
      for neighbor in graph[node]:
          if nodes[neighbor].finished:
              continue
          newDistance = distance + graph[node][neighbor]
          if newDistance<nodes[neighbor].d:
              nodes[neighbor].d=newDistance
              nodes[neighbor].parent=node
              heapq.heappush(queue,(newDistance,neighbor))

  return nodes
