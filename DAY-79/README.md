# Day 79 - Increment Submatrices by One

**Problem Link**: [LeetCode 2536 - Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/)  
**Difficulty**: Medium

## Approach

We solve this using the **2D Difference Array (Prefix Sum Technique)** — a powerful method to handle multiple range updates efficiently.

### Key Idea:
Instead of updating each cell in a submatrix (O(q × n²)), we use a **difference array** to mark only the boundaries of each query in **O(1)** time.

### Steps:
1. Create a `(n+1) × (n+1)` difference array `d` initialized with zeros.
2. For each query `[x1, y1, x2, y2]` (0-indexed):
   - `d[x1][y1] += 1` → start increment
   - `d[x1][y2+1] -= 1` → stop horizontally
   - `d[x2+1][y1] -= 1` → stop vertically
   - `d[x2+1][y2+1] += 1` → correction (inclusion-exclusion)
3. Reconstruct the final matrix using **2D prefix sum**:
   - `mat[i][j] = d[i][j] + mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]`

This is the **2D version** of the classic difference array technique.

### Example:
Query: `(1,1)` to `(2,2)` → marks four corners in `d` → final `mat` correctly shows `+1` in that submatrix.

## Complexity

- **Time**: **O(n² + q)** — `q` queries, `n²` to reconstruct
- **Space**: **O(n²)** — for difference and result matrix

## Screenshot
![Solution Screenshot](screenshot.png)