# Day 91 - Paths in Matrix Whose Sum Is Divisible by K

**Problem Link**: [LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)  
**Difficulty**: Hard

## Approach

We solve this using **DFS with Memoization** (Top-down DP) where the state is `(row, col, current_sum % k)`.

### Key Insight:
> We only care about the **sum modulo k**, not the actual sum → reduces state space dramatically.

### State:
- `r`: current row
- `c`: current column
- `rem`: current path sum modulo `k`

### Transitions:
From `(r,c)` we can go:
- Down → `(r+1, c)`
- Right → `(r, c+1)`

At each step, update remainder:  
`new_rem = (rem + grid[r][c]) % k`

### Base Cases:
- If we reach `(R-1, C-1)` → check if `(rem + grid[R-1][C-1]) % k == 0` → return `1` if yes, else `0`
- If out of bounds → return `0`

### Memoization:
Use 3D DP table: `dp[r][c][rem]` → number of valid paths from `(r,c)` with current sum ≡ `rem mod k`

### Steps:
1. Initialize `dp` as `-1` (unvisited)
2. Define recursive `dfs(r, c, rem)`
3. Memoize results to avoid recomputation
4. Return `dfs(0, 0, 0)` → paths from top-left with sum ≡ 0 mod k

### Example: `grid = [[5,2,4],[3,0,5],[0,7,2]]`, `k = 3`
→ Only paths where total sum % 3 == 0 are counted.

## Complexity

- **Time**: **O(R × C × k)** — each state computed once
- **Space**: **O(R × C × k)** — for the DP table

## Screenshot
![Solution Screenshot](screenshot.png)