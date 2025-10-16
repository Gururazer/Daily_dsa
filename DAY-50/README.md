# Day 50 - Smallest Missing Non-negative Integer After Operations

**Problem Link**: [LeetCode 2598 - Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using a frequency counting approach with modulo operations to find the smallest missing non-negative integer.

- Create a frequency array `rem` of size `value` to count how many numbers map to each remainder when divided by `value`.
- For each number `i` in `nums`, increment `rem[i % value]` to track the count of numbers that produce this remainder.
- Start from `res = 0` and check if `rem[res % value]` has a count > 0:
  - If yes, decrement the count (effectively "using" this remainder) and increment `res`.
  - Continue until `rem[res % value]` is 0, meaning no number produces this remainder.
- Return `res`, which is the smallest non-negative integer not achievable after operations.

## ⏱️ Complexity

- **Time**: O(n + m) - Where n is the length of `nums` (for counting remainders) and m is the worst-case search for the missing integer (bounded by the total possible values).
- **Space**: O(value) - For the remainder frequency array.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)