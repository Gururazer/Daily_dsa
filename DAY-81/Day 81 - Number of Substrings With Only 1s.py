class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        ans = 0

        def nsum(L):
            return (L * (L+1)) // 2 
        
        l = 0
        while l < n and s[l] != '1':
            l += 1
        r = l

        while r < n:
            while r < n and s[r] == '1':
                r += 1
            ans += nsum(r - l)
            l = r
            while l < n  and s[l] != '1':
                l += 1
            r = l

        return ans % (10**9 + 7)