class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        ans = 1
        curr = 1
        prev = set()
        
        while curr % k:
            if curr in prev:
                return -1
            prev.add(curr)
            curr = (curr % k) * 10 + 1
            ans += 1

        return ans
