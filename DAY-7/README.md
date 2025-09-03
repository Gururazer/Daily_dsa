# Day 7 - Find the Number of Ways to Place People II

**Problem Link**: [LeetCode 3027 - Find the Number of Ways to Place People II](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using a coordinate compression and 2D prefix sum approach to efficiently count valid point pairs.

- **Coordinate Compression**: Extract unique x and y coordinates, sort them, and map to indices to create a compact grid.
- **Grid Creation**: Build a grid where `grid[i][j] = 1` if a point exists at mapped coordinates `(i, j)`, else `0`.
- **Prefix Sum**: Compute a 2D prefix sum array to quickly count points in any rectangle.
- **Pair Checking**: For each pair of points `(i, j)`:
  - Ensure point `i` (Alice) is upper-left of point `j` (Bob): `x_i <= x_j` and `y_i >= y_j`.
  - Use prefix sum to count points in the rectangle formed by `(x_i, y_j)` (bottom-left) and `(x_j, y_i)` (top-right).
  - A pair is valid if the rectangle contains exactly 2 points (Alice and Bob).
- **Optimization**: Coordinate compression reduces the grid size, and prefix sum allows O(1) rectangle queries, improving efficiency over brute force.

## ⏱️ Complexity

- **Time**: O(n log n + n²), where n is the number of points (O(n log n) for sorting coordinates, O(n²) for checking pairs).
- **Space**: O(m * k), where m and k are the number of unique x and y coordinates (for the prefix sum grid).

## 📸 Screenshot
![Solution Screenshot](screenshot.png)