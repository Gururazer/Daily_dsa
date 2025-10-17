from functools import cache
class Solution:
    def maxPartitionsAfterOperations(self, S: str, K: int) -> int:
        
        CHAR = [1 << (ord(c) - ord("a")) for c in S]

        @cache
        def dp(i, opt, m1):
            if i == len(CHAR):
                return 0
            m2 = m1 | CHAR[i]
            if m2.bit_count() > K:
                ans = 1 + dp(i + 1, opt, CHAR[i])
            else:
                ans = dp(i + 1, opt, m2)

            if opt:
                for j in range(26):
                    m2 = m1 | (1 << j)
                    if m2.bit_count() > K:
                        ans = max(ans, 1 + dp(i + 1, 0, 1 << j))
                    else:
                        ans = max(ans, dp(i + 1, 0, m2))
            
            return ans

        return dp(0, 1, 0) + 1
s = Solution()
print(s.maxPartitionsAfterOperations("accca", 2)) #3