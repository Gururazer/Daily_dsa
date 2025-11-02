# Day 67 - Count Unguarded Cells in the Grid

**Problem Link**: [LeetCode 2257 - Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)  
**Difficulty**: Medium

## Approach

We solve this by simulating the guard's line of sight in four directions and marking cells as guarded.

- Create a `m × n` grid `dp` initialized with `'y'` (unguarded).
- Mark all **guard** positions with `'g'` and **wall** positions with `'w'`.
- For each guard at `(row, col)`:
  - **Left**: Traverse left until hitting a wall or guard → mark all cells as `'n'` (guarded).
  - **Right**: Traverse right until blocked.
  - **Up**: Traverse upward until blocked.
  - **Down**: Traverse downward until blocked.
- Count cells that remain `'y'` → these are **unguarded**.

## Complexity

- **Time**: **O(m × n)** — each cell is visited at most once per direction
- **Space**: **O(m × n)** — for the grid

## Screenshot
![Solution Screenshot](screenshot.png)