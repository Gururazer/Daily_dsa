class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s) > 2:
            ans = ""
            for i in range(len(s)-1):
                sum = (int(s[i]) + int(s[i+1]))  % 10
                ans += str(sum)
            s = ans    
        return s[0] == s[1]