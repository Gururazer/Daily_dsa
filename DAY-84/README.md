# Day 84 - Keep Multiplying Found Values by Two

**Problem Link**: [LeetCode 2154 - Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)  
**Difficulty**: Easy

## Approach

We solve this by **repeatedly doubling** the `original` value whenever it is found in the array using **binary search** on a sorted array.

### Steps:
1. **Sort** `nums` → enables O(log n) lookup.
2. Define a helper `bi` (binary search) that:
   - Returns `target * 2` if `target` is found.
   - Returns `-1` if not found.
3. Start with `ans = original`.
4. While `original` exists in `nums`:
   - Update `ans = original`
   - Double it: `original = original * 2`
5. Return `ans` → the last value **not present** in `nums`.

### Why it works:
- Since `nums` is sorted, we can efficiently check existence.
- We keep doubling until the value is no longer in the array.

### Example: `nums = [5,3,6,1,12]`, `original = 3`
- `3` → found → double → `6`
- `6` → found → double → `12`
- `12` → found → double → `24`
- `24` → not found → **return 24**

## Complexity

- **Time**: **O(n log n + log M)** — sorting + up to log(max_value) doublings
- **Space**: **O(1)** (if sorting in-place allowed)

## Screenshot
![Solution Screenshot](screenshot.png)