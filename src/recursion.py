# recursion

def factorial(n: int, acc: int = 1) -> int:
  if n == 1:
    return acc
  else:
    return factorial(n - 1, acc * n)

print(f'factorial of 9 should yield 362_880 == {factorial(9)}')