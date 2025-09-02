# Day 6 - Find the Number of Ways to Place People I

**Problem Link**: [LeetCode 3025 - Find the Number of Ways to Place People I](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using a sorting-based greedy approach.

- **Sort points** by x-coordinate ascending and, for the same x, y-coordinate descending to process points from left to right and higher y first.
- For each point `i` as the "top-left" point:
  - Iterate over points `j` (where `j > i`) to find valid pairs where `points[j]` is to the right (`x_j >= x_i`) and below or at the same y-level (`y_j <= y_i`).
  - Use a `ylow` variable to track the highest y-coordinate of a valid pair to ensure no points lie strictly between `points[i]` and `points[j]` in the y-range.
  - If `y_j == y_i`, break early since no further points can form a valid pair (optimization due to descending y-sort).
- Count each valid pair where `y_j <= y_i` and `y_j > ylow`, updating `ylow` to `y_j` after each valid pair.

## ⏱️ Complexity

- **Time**: O(n log n + n²), where n is the number of points (O(n log n) for sorting, O(n²) for nested loops)
- **Space**: O(1) (excluding input storage)

## 📸 Screenshot
![Solution Screenshot](screenshot.png)
