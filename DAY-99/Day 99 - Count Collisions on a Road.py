class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0 

        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        L = directions.count('L')
        R = directions.count('R')
        ans = L + R

        return ans