class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = []
        vis = set()
        sml = s

        q.append(s)
        vis.add(s)

        while(bool(q)):
            curr = q.pop(0)
            sml = min(sml,curr)

            #add opr
            crlt = list(curr)
            for _ in range(1,len(crlt),2):
                crlt[_] = str((int(crlt[_])+ a) % 10)
            addstr = "".join(crlt)
            if addstr not in vis:
                q.append(addstr)
                vis.add(addstr)
                
            #rot opr
            rotstr = curr[b:] + curr[:b]
            if rotstr not in vis:
                q.append(rotstr)
                vis.add(rotstr)
        
        return sml
    
s = Solution()
print(s.findLexSmallestString(s = "5525", a = 9, b = 2))