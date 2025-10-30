# Day 64 - Minimum Number of Increments on Subarrays to Form a Target Array

**Problem Link**: [LeetCode 1526 - Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)  
**Difficulty**: Hard

## Approach

We solve this using a greedy observation: **the number of operations needed equals the sum of all positive differences when moving from left to right**.

- Initialize `res = 0` (total operations) and `prev = 0` (previous height).
- For each element `i` in `target`:
  - If `i > prev`, we need to **increase** the subarray ending at current index by `i - prev`.
  - Add `i - prev` to `res`.
  - Update `prev = i`.
- **Key Insight**: When `i < prev`, no new operation is needed — the previous increment already covers the current height.
- Return `res`.

> Example:  
> `target = [1,3,2,4]` → Operations:  
> - `1` → +1  
> - `3` → +2 (from 1 to 3)  
> - `2` → no new op (already covered)  
> - `4` → +2 (from 2 to 4)  
> Total = 5

## Complexity

- **Time**: **O(n)** — single pass through the array
- **Space**: **O(1)** — only two variables used

## Screenshot
![Solution Screenshot](screenshot.png)