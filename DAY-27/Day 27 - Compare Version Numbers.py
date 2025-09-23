class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = [int(v) for v in version1.split('.')]
        s2 = [int(v) for v in version2.split('.')]   
        n1, n2 = len(s1), len(s2)
        maxLength = max(n1, n2)
        
        for i in range(maxLength):
        
            rev1 = s1[i] if i < n1 else 0
            rev2 = s2[i] if i < n2 else 0

            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0