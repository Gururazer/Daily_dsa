# Day 97 - Count Number of Trapezoids I

**Problem Link**: [LeetCode 3623 - Count Number of Trapezoids I](https://leetcode.com/problems/count-number-of-trapezoids-i/)  
**Difficulty**: Hard

## Approach

We solve this by **exploiting a key geometric property**:  
A **trapezoid** with **exactly two parallel sides** (horizontal) is formed by choosing **two distinct y-levels** and **any two points** — one from each level.

### Key Insight:
> As long as there are **at least two points** on each of two different `y`-levels,  
> every pair `(point from y1, point from y2)` forms a valid trapezoid  
> (since the two horizontal lines at `y1` and `y2` are parallel).

### Steps:
1. Group points by their `y`-coordinate using a dictionary `ymp`.
2. If fewer than 2 distinct `y`-levels → return `0`.
3. For each `y`, compute number of ways to choose 2 points on that level:  
   `C(count, 2) = count * (count - 1) // 2`
4. Sort the `y`-levels and compute:
   - `posx[i]`: number of valid pairs on level `i`
   - `pref[i]`: cumulative sum of pairs up to level `i`
5. For each level `i`:
   - All pairs on level `i` can form a trapezoid with **all pairs on levels > i**
   - Number = `posx[i] * (total_pairs_after_i)`
   - `total_pairs_after_i = pref[-1] - pref[i]`
6. Sum over all `i` → total trapezoids
7. Return result modulo `10^9 + 7`

### Example:
`points = [[1,1],[2,1],[3,1],[1,2],[2,2],[4,2]]`
- y=1: 3 points → C(3,2) = 3
- y=2: 3 points → C(3,2) = 3
- Trapezoids = 3 × 3 = **9**

All possible pairs across two horizontal lines!

## Complexity

- **Time**: **O(n + m log m)** — grouping + sorting m distinct y-levels
- **Space**: **O(m)** — for frequency map and prefix

## Screenshot
![Solution Screenshot](screenshot.png)