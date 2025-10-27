from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        n = len(bank)
        if n < 2:
            return 0
        
        curr = 0
        next = curr + 1
        ans = 0

        while next < n:
            n1 = bank[curr].count('1')

            n2 = bank[next].count('1')

            while n2 < 1 and next < n - 1:
                next += 1
                n2 = bank[next].count('1')
            ans += n1 * n2

            curr = next
            next = curr + 1
        
        return ans
s = Solution()
print(s.numberOfBeams(["011001","000000","010100","001000"])) #8    