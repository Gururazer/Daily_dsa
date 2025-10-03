# Day 37 - Trapping Rain Water II

**Problem Link**: [LeetCode 407 - Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)  
**Difficulty**: Hard

## 💡 Approach

We solve this using a priority queue (min-heap) to simulate water trapping in a 2D height map by processing boundaries inward.

- If the height map is empty, return 0.
- Initialize a min-heap with boundary cells (first/last rows and columns), storing `(height, row, col)` tuples.
- Mark boundary cells as visited in a `visited` matrix.
- Use directions (up, down, left, right) to explore neighboring cells.
- While the heap is not empty:
  - Pop the cell with the minimum height.
  - For each unvisited neighbor:
    - Mark as visited.
    - Calculate trapped water as `max(0, heap_height - neighbor_height)`.
    - Add trapped water to `total_water`.
    - Push the neighbor to the heap with height `max(heap_height, neighbor_height)` to ensure water level consistency.
- Return `total_water`.

## ⏱️ Complexity

- **Time**: O(m * n * log(m * n)) - Where m and n are the dimensions of the height map. Heap operations take O(log(m * n)) for up to m * n cells.
- **Space**: O(m * n) - For the visited matrix and min-heap.

## 📸 Screenshot
![Solution Screenshot](screenshot.png)