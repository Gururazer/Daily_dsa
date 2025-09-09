class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        new_people = [0] * (n + 1)
        new_people[1] = 1
        sharing = 0
        total_aware = 1

        for day in range(2, n + 1):
            if day > delay:
                sharing = (sharing + new_people[day - delay]) % mod
            
            if day > forget:
                sharing = (sharing - new_people[day - forget] + mod) % mod
                total_aware = (total_aware - new_people[day - forget] + mod) % mod
            
            newly_aware_today = sharing
            new_people[day] = newly_aware_today
            total_aware = (total_aware + newly_aware_today) % mod
        
        return total_aware