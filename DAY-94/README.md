# Day 94 - Minimum Operations to Make Array Sum Divisible by K

**Problem Link**: [LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/)  
**Difficulty**: Easy

## Approach

We solve this in **one line** using a brilliant observation:

> The **minimum number of operations** needed to make the sum divisible by `k` is **exactly** the **current sum modulo `k`**.

### Why?

Let:
- `S = sum(nums)`
- `r = S % k`

Then:
- If `r == 0` → already divisible → **0 operations**
- Else → we need to **reduce** the sum by `r` to reach the next multiple of `k` below it.

And since we can **decrease** any element by any amount (even down to 0), the **minimum** total reduction is exactly `r`.

We **cannot** do it in fewer operations because we need to reduce the sum by at least `r`.

### Example:
- `nums = [1,2,3,4]`, `k = 5`
- `S = 10`, `10 % 5 = 0` → return `0`
- `nums = [1,2,3,4]`, `k = 6`
- `S = 10`, `10 % 6 = 4` → return `4`
  - Reduce one number by 4 → sum becomes 6 → divisible by 6

### Proof:
- You need to reduce sum by a multiple of `k` → smallest non-zero is `k`
- But `r` is the smallest amount that brings you to a multiple of `k`
- `r < k` → so it's **always better** than reducing by `k`

Hence: `min operations = S % k`

## Complexity

- **Time**: **O(n)** — to compute sum
- **Space**: **O(1)**

## Screenshot
![Solution Screenshot](screenshot.png)