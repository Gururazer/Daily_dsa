class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        opts = 0
        while n:
            opts ^= n
            n >>= 1

        return opts
