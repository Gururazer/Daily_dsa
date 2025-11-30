# Day 95 - Make Sum Divisible by P

**Problem Link**: [LeetCode 1590 - Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/)  
**Difficulty**: Medium

## Approach

We solve this using **Prefix Sum + Hash Map** — a classic technique for finding subarrays with a target sum modulo `p`.

### Key Insight:
> We want to **remove** the **shortest** subarray such that the remaining sum is divisible by `p`.

Let:
- `total = sum(nums)`
- `r = total % p`

We need to remove a subarray whose sum ≡ `r mod p` → then remaining sum ≡ `0 mod p`.

So we look for a subarray with sum ≡ `r mod p`.

### Using Prefix Sums:
Let `pref[i]` = sum of first `i` elements **mod p**

We want:
> `pref[j] - pref[i] = r mod p`  
> → `pref[j] - r ≡ pref[i] mod p`

So for each `j`, we look for the **largest** `i < j` such that:
> `pref[i] ≡ (pref[j] - r) mod p`

→ This gives us the **longest** valid prefix before `j`, hence the **shortest** subarray to remove.

### Steps:
1. If `total % p == 0` → return `0` (no need to remove anything)
2. Use a map `mp` to store: `prefix_mod → last_index`
   - Initialize `mp[0] = -1` (before index 0)
3. Traverse the array:
   - Update `pref = (pref + nums[i]) % p`
   - Compute target = `(pref - r) % p`
   - If `target` in `mp` → we found a valid subarray → update `res`
   - Update `mp[pref] = i`
4. Return `res` if smaller than `n`, else `-1`

### Example:
`nums = [3,1,4,2]`, `p = 6`
- total = 10 → 10 % 6 = 4 → need to remove subarray sum ≡ 4
- At i=2: pref = 8 % 6 = 2 → target = (2 - 4) % 6 = 4
- We saw prefix mod 4 before → remove subarray → length = 3 → but smaller exists
- Final answer: remove `[4]` → length **1**

## Complexity

- **Time**: **O(n)**
- **Space**: **O(n)**

## Screenshot
![Solution Screenshot](screenshot.png)