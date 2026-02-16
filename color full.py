st = input()
ins = input()
lis_st = 1
a = 0
b = 0
for i in range(len(ins)):
    if st[a] == ins[b]:
        lis_st += 1
        a += 1
        b += 1
    else:
        b += 1    
        
        
print(lis_st)  

