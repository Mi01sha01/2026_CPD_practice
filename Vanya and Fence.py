n, h = map(int, input().split())
heights = list(map(int, input().split()))

width_of_road = 0
for height in heights:
    if height > h:
        width_of_road += 2
    else:
        width_of_road += 1
print(width_of_road)            