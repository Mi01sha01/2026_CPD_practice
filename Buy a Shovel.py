k, r = map(int, input().split())

min_num_of_shovels = 1
num_of_shovels = 1
cost = k

while (cost % 10 != 0) and ( cost % 10 != r):
    min_num_of_shovels += 1
    num_of_shovels += 1
    cost = k * num_of_shovels

print(min_num_of_shovels)
