# Day 92 - Maximum Subarray Sum With Length Divisible by K

**Problem Link**: [LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K](https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/)  
**Difficulty**: Hard

## Approach

We solve this using **prefix sums + modulo tracking** — a brilliant variation of Kadane’s algorithm.

### Key Insight:
> We want a subarray `nums[i..j]` such that:
> - `j - i + 1` is divisible by `k`
> - Sum is maximized

This is equivalent to:
> `(j + 1) % k == (i) % k`  
> → both prefix indices have **same remainder** when divided by `k`

So:
> `sum[i+1..j+1] = prefix[j+1] - prefix[i]`  
> → To maximize this → **maximize** `prefix[j+1]` and **minimize** `prefix[i]` with same `(index % k)`

### Steps:
1. `pref` = running prefix sum
2. `mem[rem]` = **minimum** prefix sum seen so far with index length ≡ `rem mod k`
   - We store **minimum** because we want to **maximize** `pref - mem[rem]`
3. For each position `i`:
   - Compute length so far: `R = i + 1`
   - `rem = R % k`
   - If we’ve seen a previous prefix with same `rem` → we have a valid subarray
   - Update `ans = max(ans, pref - mem[rem])`
   - Then **update** `mem[rem] = min(mem[rem], pref)`

> Note: We update `mem` **after** checking to allow using earlier (smaller) prefixes.

### Example:
`nums = [1, -2, 3, 4]`, `k = 2`
- Lengths 2 and 4 are valid
- At i=1 (length=2): rem=0 → `pref = -1`, `mem[0]=0` → sum = -1 - 0 = -1
- At i=3 (length=4): rem=0 → `pref = 6`, `mem[0]=-1` → sum = 6 - (-1) = **7**

## Complexity

- **Time**: **O(n)**
- **Space**: **O(k)**

## Screenshot
![Solution Screenshot](screenshot.png)