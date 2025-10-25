class Solution:
    def totalMoney(self, n: int) -> int:
        
        sum = 0
        w = n // 7
        rem = 7 - (n % 7) 
        #figure out the no of weeks
        i = 0
        num = 7
        while(i < w):
            sum += ((num*(num+1))// 2) - ((i*(i+1))//2)
            i += 1
            num += 1
        
        
        sum += ((num*(num+1))// 2) - ((i*(i+1))//2)
        
        for _ in range(rem):
            sum -= num
            num -= 1 
        

        return sum

         
        
        

s = Solution()
print(s.totalMoney(10)) # 37     
print(s.totalMoney(26)) # 135     
print(s.totalMoney(20)) # 96  
