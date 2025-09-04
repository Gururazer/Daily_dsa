class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        n1 = abs(z - x)
        n2 = abs(z - y)
        if n1 > n2:
            return 2
        elif n1 == n2:
            return 0
        return 1
        
        