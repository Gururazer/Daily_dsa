# Day 39 - Pacific Atlantic Water Flow

**Problem Link**: [LeetCode 417 - Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)  
**Difficulty**: Medium

## 💡 Approach

We solve this using DFS to find cells reachable by water flowing to both Pacific and Atlantic oceans.

- If the height map is empty, return an empty list.
- Initialize two sets: `pacific_reachable` and `atlantic_reachable` to track cells reachable from each ocean.
- Define a DFS function to explore cells where water can flow (next cell height ≥ current cell height):
  - Add the current cell to the reachable set.
  - Explore four directions (up, down, left, right) if within bounds and next cell height is sufficient.
- Run DFS from Pacific borders (first row and first column) to populate `pacific_reachable`.
- Run DFS from Atlantic borders (last row and last column) to populate `atlantic_reachable`.
- Collect cells present in both sets as the result (cells where water can flow to both oceans).

## ⏱️ Complexity

- **Time**: O(m * n) - Each cell is visited at most twice (once per ocean) using DFS, where m and n are the dimensions of the height map.
- **Space**: O(m * n) - For the reachable sets and recursion stack.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)