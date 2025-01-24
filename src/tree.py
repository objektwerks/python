# tree

from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")

@dataclass
class TreeNode(Protocol[T]):
  data: T
  left: T
  right: T

# TODO - not sure this approach works in Python ( 2025.1.24 )