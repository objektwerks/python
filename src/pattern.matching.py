# pattern matching

def matchOn(i: int) -> str:
  match i:
      case 0: return 'zero'
      case 1: return 'one'
      case 2: return 'two'
      case 3: return 'three'
      case _: return 'unknown'
  
print(f'match on 0 to {matchOn(0)}')