from typing import List
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        end = 1
        while(end < len(words)):
            srt1 = sorted(words[end])
            srt2 = sorted(words[end-1])
            if srt1 == srt2:
                del words[end]
            else:
                end += 1
        
        return words

s = Solution()
print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"])) # ["abba","cd"]
