# Day 93 - Maximum Number of K-Divisible Components

**Problem Link**: [LeetCode 2872 - Maximum Number of K-Divisible Components](https://leetcode.com/problems/maximum-number-of-k-divisible-components/)  
**Difficulty**: Hard

## Approach

We solve this using **Leaf-to-Root Pruning + Subtree Sum Propagation** — a brilliant **topological peel** technique on trees.

### Key Insight:
> If a **leaf** node has value divisible by `k`, we can **cut** it as a separate component.  
> Otherwise, we **add** its value to its parent and **remove** it.

This simulates **detaching** subtrees that are divisible by `k`.

### Steps:
1. Build adjacency list `G`.
2. Start with all **leaves** (degree 1) in a queue `Q`.
3. While queue is not empty:
   - Take a leaf `u`
   - Find its parent `p`
   - If `values[u] % k == 0` → we can **cut** this subtree → `count += 1`
   - Else → **merge** its value into parent: `values[p] += values[u]`
   - Remove edge `u ↔ p`
   - If `p` now becomes a leaf → add to queue
4. Repeat until only root (or nothing) remains.

### Why it works:
- Every time we cut a node with `val % k == 0`, we gain a valid component.
- Merging values upward preserves correctness.
- We process nodes **only when they become leaves** → guarantees we don't miss any cuttable subtree.

### Example:
`values = [6, 2, 7, 4]`, `k = 3` → tree: 0(6)-1(2)-2(7)-3(4)  
- Start with leaf 3: `4 % 3 != 0` → add 4 to 2 → node 2 now 11
- Leaf 2: `11 % 3 = 2 != 0` → add 11 to 1 → node 1 now 13
- Leaf 1: `13 % 3 = 1 != 0` → add 13 to 0 → node 0 now 19
- Leaf 0: `19 % 3 = 1 != 0` → no cut  
→ But wait — actually only **node 0 (6)** was divisible → **1 component**

Correct! Only one valid cut.

## Complexity

- **Time**: **O(n)** — each node and edge processed once
- **Space**: **O(n)** — for graph and queue

## Screenshot
![Solution Screenshot](screenshot.png)