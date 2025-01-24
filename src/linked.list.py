# linked list

from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")

@dataclass
class Node(Protocol[T]):
  data: T
  next: T

@dataclass
class LinkedList(Node[T]):
  head: Node[T]
  tail: list[Node[T]]

# TODO - not sure this approach works in Python ( 2025.1.24 )
