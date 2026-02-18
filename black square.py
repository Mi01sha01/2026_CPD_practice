def solve():
        
        calories = list(map(int, input().split()))
        s = input()
        
        wasted_calories = 0
        
        for i in s:
            index = int(i) - 1
            
            wasted_calories += calories[index]
            
        print(wasted_calories)
solve()        