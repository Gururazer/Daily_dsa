# Day 30 - Valid Triangle Number

**Problem Link**: [LeetCode 611 - Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using a two-pointer technique after sorting the array to count valid triangles.

- Sort the input array `nums` in ascending order.
- If the array length is less than 3, return 0 (no triangles possible).
- Iterate `k` from the end to index 2 (largest side of the triangle).
- For each `k`, use two pointers `i` (starting from 0) and `j` (starting from `k-1`):
  - If `nums[i] + nums[j] > nums[k]`, all pairs between `i` and `j` form valid triangles with `nums[k]` (since the array is sorted), so add `j - i` to the count and decrement `j`.
  - Otherwise, increment `i` to try a larger value.
- Return the total count of valid triangles.

## ⏱️ Complexity

- **Time**: O(n²) - Sorting takes O(n log n), and the two-pointer loop takes O(n²) in the worst case, where n is the length of `nums`.
- **Space**: O(1) - No extra space beyond input storage (assuming in-place sorting).

## 📸 Screenshot
![Solution Screenshot](screenshot.png)