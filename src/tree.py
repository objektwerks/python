# tree

from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")

@dataclass
class Node(Protocol[T]):
  data: T

@dataclass
class Tree(Node[T]):
  left: Node[T]
  righ: Node[T]

# TODO - not sure this approach really works in Python ( 2025.1.24 )