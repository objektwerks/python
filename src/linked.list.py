# linked list

from dataclasses import dataclass
from typing import Protocol, TypeVar

T = TypeVar("T")

@dataclass
class Node(Protocol[T]):
  data: T
  next: T

@dataclass
class LinkedList(Protocol[T]):
  head: T
  tail: list[T]

  @staticmethod
  def build(items: list[T]) -> None:
    len: int = len(items)
    if len > 0:
      head = items[0]
      if len > 1:
        tail = list[T][1:len - 1]