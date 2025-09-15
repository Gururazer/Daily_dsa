class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        LS = text.split()
        bl = set(brokenLetters)
        cnt = 0
        for word in LS:
            for letter in word:
                if letter in bl:
                   cnt += 1
                   break
        return len(LS) - cnt            