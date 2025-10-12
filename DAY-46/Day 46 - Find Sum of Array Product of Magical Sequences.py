class Solution:
    def sumOfArrayProduct(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        powers = [[1] * (m + 1) for _ in range(n)]
        for j in range(n):
            for c in range(1, m + 1):
                powers[j][c] = (powers[j][c-1] * nums[j]) % MOD

        MAX_M = m
        fact = [1] * (MAX_M + 1)
        inv_fact = [1] * (MAX_M + 1)
        
        def power(a, b, mod):
            res = 1
            a %= mod
            while b > 0:
                if b & 1:
                    res = (res * a) % mod
                a = (a * a) % mod
                b >>= 1
            return res

        for i in range(1, MAX_M + 1):
            fact[i] = (fact[i-1] * i) % MOD
            
        inv_fact[MAX_M] = power(fact[MAX_M], MOD - 2, MOD)
        for i in range(MAX_M - 1, 0, -1):
            inv_fact[i] = (inv_fact[i+1] * (i + 1)) % MOD
            
        def nCr_mod(n, r):
            if r < 0 or r > n:
                return 0
            return (((fact[n] * inv_fact[r]) % MOD) * inv_fact[n - r]) % MOD

        dp_prev = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
        dp_prev[0][0][0] = 1

        for j in range(n):
            dp_curr = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
            
            for c_old in range(m + 1):
                for b_old in range(m + 1):
                    for k_old in range(k + 1):
                        if dp_prev[c_old][b_old][k_old] == 0:
                            continue
                        
                        for c_j in range(m - c_old + 1):
                            c_new = c_old + c_j
                            quantity_j = c_j + b_old
                            bit_j = quantity_j % 2
                            b_new = quantity_j // 2
                            k_new = k_old + bit_j
                            
                            if k_new > k:
                                continue
                            
                            prod_factor = powers[j][c_j]
                            comb_factor = nCr_mod(m - c_old, c_j)
                            
                            contribution = dp_prev[c_old][b_old][k_old]
                            contribution = (contribution * prod_factor) % MOD
                            contribution = (contribution * comb_factor) % MOD
                            
                            dp_curr[c_new][b_new][k_new] = (dp_curr[c_new][b_new][k_new] + contribution) % MOD

            dp_prev = dp_curr

        max_extra_steps = 6 
        for _ in range(max_extra_steps):
            dp_curr = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(m + 1)]
            
            for b_old in range(m + 1):
                for k_old in range(k + 1):
                    if dp_prev[m][b_old][k_old] == 0:
                        continue
                    
                    quantity_j = b_old
                    bit_j = quantity_j % 2
                    b_new = quantity_j // 2
                    k_new = k_old + bit_j
                    
                    if k_new > k:
                        continue
                        
                    dp_curr[m][b_new][k_new] = (dp_curr[m][b_new][k_new] + dp_prev[m][b_old][k_old]) % MOD

            dp_prev = dp_curr
            if sum(sum(dp_prev[m][b_new]) for b_new in range(1, m + 1)) == 0:
                 break
        
        return dp_prev[m][0][k]