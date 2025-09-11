class Solution:
    def sortVowels(self, s: str) -> str:
        L1 = list()
        L2 = list()
        vow = ['a','e','i','o','u','A','E','I','O','U']
        for idx, val in enumerate(s):
            if val in vow:
               L1.append(idx)
               L2.append(val)
        L2 = sorted(L2, reverse = True)
        j = len(L2) - 1
        s = list(s)
        for i in L1:
            s[i] = L2[j]
            j -= 1 
        return "".join(s)