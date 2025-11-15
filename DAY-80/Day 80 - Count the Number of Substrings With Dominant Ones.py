class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        nextz = [n] * n

        for i in range(n-2,-1,-1):
            if s[i+1] == '0':
                nextz[i] = i + 1
            else:
                nextz[i] = nextz[i + 1]

        res = 0
        for l in range(n):
            zeroes = 1 if s[l] == '0' else 0
            r = l

            while zeroes*zeroes <= n:
                nxtz = nextz[r]
                ones = (nxtz - l) - zeroes
                if ones >= zeroes*zeroes:
                    res += min(
                        nxtz - r,
                        ones - zeroes*zeroes + 1
                    )
                
                r = nxtz
                zeroes += 1
                if r == n:
                    break


        return res