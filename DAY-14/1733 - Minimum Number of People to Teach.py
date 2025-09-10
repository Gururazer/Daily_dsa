import collections

class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        user_languages_sets = [set(langs) for langs in languages]
        
        
        uncommunicative_pairs = []
        for u, v in friendships:
            u_idx, v_idx = u - 1, v - 1
            
            
            if not user_languages_sets[u_idx].intersection(user_languages_sets[v_idx]):
                uncommunicative_pairs.append((u_idx, v_idx))
        
        
        if not uncommunicative_pairs:
            return 0
            
        min_teach_count = float('inf')
        
        
        for lang_to_teach in range(1, n + 1):
            
            users_to_teach = set()
            
            for u_idx, v_idx in uncommunicative_pairs:
                
                if lang_to_teach not in user_languages_sets[u_idx]:
                    users_to_teach.add(u_idx)
                
                
                if lang_to_teach not in user_languages_sets[v_idx]:
                    users_to_teach.add(v_idx)
            
            
            current_teach_count = len(users_to_teach)
            
            
            min_teach_count = min(min_teach_count, current_teach_count)
            
        return min_teach_count