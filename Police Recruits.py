def solve():
        n = int(input())
        events = list(map(int, input().split()))
        
        num_of_police = 0
        num_of_untreated_crime = 0
        
        for i in events:
            if i == -1:
                if num_of_police > 0:
                    num_of_police -= 1
                else:
                    num_of_untreated_crime += 1
                        
            else:
                num_of_police += i 
                
        print(num_of_untreated_crime)      
            
        
solve()        