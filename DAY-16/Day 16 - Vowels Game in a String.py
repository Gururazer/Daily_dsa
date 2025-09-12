class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow = ['a','e','i','o','u']
        for _ in vow:
            if _ in s:
                return True
        else:
            return False