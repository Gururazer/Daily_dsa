# Day 85 - Set Intersection Size At Least Two

**Problem Link**: [LeetCode 757 - Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/)  
**Difficulty**: Hard

## Approach

We solve this using a **greedy algorithm** with **sorting by end point** — a classic technique for interval covering problems.

### Key Insight:
> To minimize the total number of points while ensuring every interval contains **at least 2 points** from our set, we should **greedily place points as late as possible**.

### Steps:
1. **Sort intervals by their end point** (`x[1]`) → process intervals that end earliest first.
2. Maintain a list `c` of the **last two points** placed in the current intersection.
3. For each interval `[s, e]`:
   - If `s > c[1]` → current two points are **completely left** of interval → need to place **two new points**: `e-1` and `e`
   - Else if `s > c[0]` → only the largest point is in range → place **one new point** at `e`
     - Update `c` to `[old largest, e]` (or `[e-1, e]` if `e` is used)
   - Else → both points already cover this interval → do nothing

### Greedy Justification:
> By placing points as far right as possible, we maximize their coverage for future intervals.

### Example: `intervals = [[1,3],[2,4],[3,5]]`
- After sorting by end: `[[1,3],[2,4],[3,5]]`
- First `[1,3]` → place `2,3` → `c = [2,3]`
- Second `[2,4]` → `2` is covered → place `4` → `c = [3,4]`
- Third `[3,5]` → both covered → done  
→ Total: **3 points**

## Complexity

- **Time**: **O(n log n)** — sorting + O(n) traversal
- **Space**: **O(1)** — only storing two points

## Screenshot
![Solution Screenshot](screenshot.png)