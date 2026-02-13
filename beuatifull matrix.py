def solve():
  for i in range(5):
    r = list(map(int, input().split()))
    
    
    
    if 1 in r:
      x, y = i, r.index(1)
      
  m = abs(x - 2) + abs(y - 2)
  print(m)  
    
solve()  
