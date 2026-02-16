
n = int(input())
l = list(map(int, input().split()))

for i in range(int(input())):
    x, y = map(int, input().split())
    a = x - 1
    if a - 1 >= 0:
      l[a-1] += y - 1
    if a + 1 < n:  
      l[a+1] += (l[a] - y)
    l[a] = 0
    
for i in l:
    print(i)
    
    
    
