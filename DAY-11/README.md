# Day 11 - Find N Unique Integers Sum up to Zero

**Problem Link**: [LeetCode 1304 - Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)  
**Difficulty**: Easy  
**Topics**: Array, Math  
**Companies**: Premium (Locked)  
**Status**: Solved

## 💡 Approach

The problem requires generating an array of `n` unique integers that sum to zero. The solution uses a simple and efficient approach:

- Create an empty list to store the result.
- Iterate from `1` to `n // 2` (integer division to handle both even and odd `n`):
  - For each integer `i`, append `i` and `-i` to the list. This ensures pairs of numbers that sum to zero.
- If `n` is odd, append a single `0` to the list to account for the extra number needed.
- Return the resulting list, which contains `n` unique integers summing to zero.

## ⏱️ Complexity

- **Time**: O(n) - The loop runs `n // 2` times, and appending elements is O(1).
- **Space**: O(n) - The space required to store the output array of `n` integers.

## 📸 Screenshot
![Screenshot Placeholder](screenshot.png)