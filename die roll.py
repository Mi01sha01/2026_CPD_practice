import math 
y, w = map(int, input().split())

a = 7 - max(y, w)
b = math.gcd(a, 6)

print(f'{a//b}/{6//b}')