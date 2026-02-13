s = input()
 
l = 0
 
for char in s:
  if char.islower():
    l += 1
    
a = len(s) - l
if a > l:
 print(s.upper())
 
else:
 print(s.lower())
