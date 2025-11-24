# Day 89 - Binary Prefix Divisible By 5

**Problem Link**: [LeetCode 1018 - Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)  
**Difficulty**: Easy

## Approach

We solve this by **simulating the binary number construction modulo 5** — no need to store the full number!

### Key Insight:
> Instead of building the actual prefix (which can be up to 10^3 bits → too large),  
> we only need to track the **current value modulo 5**.

Because:
> `(a * 2 + b) mod 5 = ((a mod 5) * 2 + b) mod 5`

So we can maintain a running variable `c` representing the current prefix **mod 5**.

### Steps:
1. Initialize:
   - `c = 0` → current prefix value mod 5
   - `ans = []` → result list
2. For each bit `i` in `nums`:
   - Update: `c = (c * 2 + i) % 5`
   - If `c == 0` → current prefix is divisible by 5 → append `True`
   - Else → append `False`
3. Return `ans`

### Example: `nums = [0,1,1]`
- `0` → `c = 0` → `True`
- `01` = 1 → `c = (0*2 + 1) % 5 = 1` → `False`
- `011` = 3 → `c = (1*2 + 1) % 5 = 3` → `False`
→ `[True, False, False]`

### Why modulo 5?
We only care if the number is divisible by 5 → only the remainder matters.

## Complexity

- **Time**: **O(n)** — single pass
- **Space**: **O(1)** extra (excluding output)

## Screenshot
![Solution Screenshot](screenshot.png)