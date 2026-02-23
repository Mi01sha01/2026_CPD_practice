n = int(input())
guest_uniform = []
home_uniform = []
num_of_change = 0


for _ in range(n):
    h, g = map(int, input().split())
    home_uniform.append(h)
    guest_uniform.append(g)

un = set(guest_uniform)


for i in un:
    
    c1 = home_uniform.count(i)
    c2 = guest_uniform.count(i)
    num_of_change += c1 * c2
print(num_of_change)
