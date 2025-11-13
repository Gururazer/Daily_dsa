class Solution:
    def maxOperations(self, s: str) -> int:
        n = -len(s)-1 

        ans = 0        
        prev = 0

        end = -1
        while end > n and s[end] == '1':
            end -= 1
        
        while end >= n+1:
                            
            while end > n and s[end] == '0':
                end -= 1                
            prev += 1
            while end > n and s[end] == '1':
                ans += prev
                end -= 1
            
            
        return ans