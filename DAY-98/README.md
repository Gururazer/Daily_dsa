# Day 98 - Count Number of Trapezoids II

**Problem Link**: [LeetCode 3625 - Count Number of Trapezoids II](https://leetcode.com/problems/count-number-of-trapezoids-ii/)  
**Difficulty**: Hard

## Approach

We solve this by **counting all possible trapezoids** (exactly two parallel sides) using **line equation normalization** and **hashing**.

### Key Insight:
> A trapezoid has **exactly one pair of parallel sides**.  
> We can:
> 1. Count **all quadrilaterals** with **at least one pair of parallel sides**
> 2. Subtract **rectangles and parallelograms** (which have **two** pairs of parallel sides) → they are overcounted

But the elegant solution:  
Count **all sets of 4 points** that lie on **two parallel lines**, then subtract the cases where they lie on **two different pairs** of parallel lines.

### Steps:
1. For every pair of points `(x1,y1)` → `(x2,y2)`:
   - Compute direction vector: `(dx, dy)`
   - Normalize direction using **GCD**: `(sx, sy) = (dx/g, dy/g)`
   - To handle direction invariance → if `dx < 0` or `(dx==0 and dy<0)` → flip sign
   - Compute **line equation**: `sx*y - sy*x = constant` → `de = sx*y1 - sy*x1`
   - Use `(sx, sy)` as **slope key**, `de` as **intercept**

2. Two dictionaries:
   - `td`: normalized direction → intercept → count of edges
   - `vd`: raw (dx,dy) → intercept → for detecting opposite directions

3. For each slope group:
   - All edges with same slope are **parallel**
   - For each slope, count number of ways to pick two different intercepts → each pair forms a trapezoid strip
   - Total edges on slope = `tot`, then `ans += val * (tot - val)` for each intercept group

4. Final answer:
   - `count(td)` → all trapezoids (including parallelograms)
   - `count(vd)//2` → counts each parallelogram twice (once per direction)
   - So: `count(td) - count(vd)//2` → **only trapezoids with exactly one parallel pair**

### Example:
Four points forming a trapezoid → counted once  
Four points forming a parallelogram → counted twice → subtracted → removed

## Complexity

- **Time**: **O(n²)** — we check every pair of points
- **Space**: **O(n²)** — in worst case, many unique lines

## Screenshot
![Solution Screenshot](screenshot.png)