class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        
        def normalize_vowels(word: str) -> str:
            vowels = "aeiou"
            res = []
            for char in word:
                if char in vowels:
                    res.append('*')
                else:
                    res.append(char)
            return "".join(res)

        
        word_set = set(wordlist)
        case_insensitive_map = {}
        vowel_error_map = {}
        
        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insensitive_map:
                case_insensitive_map[lower_word] = word
            
            normalized_word = normalize_vowels(lower_word)
            if normalized_word not in vowel_error_map:
                vowel_error_map[normalized_word] = word
        
        ans = []
        for query in queries:
            
            if query in word_set:
                ans.append(query)
                continue
            
            lower_query = query.lower()
            
            
            if lower_query in case_insensitive_map:
                ans.append(case_insensitive_map[lower_query])
                continue
            
            
            normalized_query = normalize_vowels(lower_query)
            if normalized_query in vowel_error_map:
                ans.append(vowel_error_map[normalized_query])
                continue
            
            
            ans.append("")
            
        return ans