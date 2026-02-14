    n = int(input())
    cards = list(map(int, input().split()))
    s = 0
    d = 0
                         
    l = 0
    r = -1
         
    for i in range(n):
       if i % 2 == 0:
         if cards[l] > cards[r]:
           s += cards[l]
           l+=1
         else:
           s += cards[r]
           r-=1
       else:
         if cards[l] > cards[r]:
           d += cards[l]
           l+=1
         else:
           d += cards[r]
           r-=1
            
    print(s,d)
