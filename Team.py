num_of_problems = 0
for _ in range(int(input())):
  view = sum(list(map(int, input().split())))
  
 
  
  if view > 1:
    num_of_problems += 1
    
print(num_of_problems)
