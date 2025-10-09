class Solution:
    def minTimeToBrewPotions(self, skill, mana):
        n, m = len(skill), len(mana)
        avail = [0] * n  

        for j in range(m):
            
            offsets = [0] * (n + 1)
            for i in range(n):
                offsets[i+1] = offsets[i] + skill[i] * mana[j]

            
            t = max(avail[i] - offsets[i] for i in range(n))
            if t < 0:
                t = 0

            
            for i in range(n):
                avail[i] = t + offsets[i+1]

        return avail[-1]


