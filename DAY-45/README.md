# Day 45 - Maximum Total Damage With Spell Casting

**Problem Link**: [LeetCode 3186 - Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using dynamic programming with memoization and binary search to maximize total damage.

- Use a `Counter` to count the frequency of each spell power in `power`.
- Sort unique spell powers to create an ordered list.
- Define a memoized DP function `dp(i)` that computes the maximum damage starting from index `i`:
  - Base case: If `i` exceeds the length of `power`, return 0.
  - For each index `i`, consider two choices:
    - **Leave**: Skip the current power and compute `dp(i + 1)`.
    - **Take**: Use binary search (`bisect_right`) to find the next valid power (greater than `power[i] + 2`) and compute damage as `cnt[power[i]] * power[i] + dp(take)`.
  - Return the maximum of leave and take options.
- Return `dp(0)` for the maximum total damage.

## ⏱️ Complexity

- **Time**: O(n log n) - Sorting takes O(n log n), binary search takes O(log n) per state, and there are O(n) states with memoization.
- **Space**: O(n) - For the Counter, sorted power list, and memoization cache.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)