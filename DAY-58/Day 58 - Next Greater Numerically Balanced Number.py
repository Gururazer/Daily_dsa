from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(i : int) -> bool:
            for num,cnt in Counter(str(i)).items():
                if num != str(cnt):
                    return False
            return True
        
        bal = []
        for i in range(n,1224445):
            if check(i):
                bal.append(i)
                if i > n:
                    break
        
        return bal[-1]
        
        
s = Solution()
print(s.nextBeautifulNumber(666666))     


