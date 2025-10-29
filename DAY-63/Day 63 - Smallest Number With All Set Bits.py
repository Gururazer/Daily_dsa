class Solution:
    def smallestNumber(self, n: int) -> int:
        s = bin(n)
        l = len(s) - 2
        return (2**l) - 1
        