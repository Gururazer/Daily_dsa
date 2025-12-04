# Day 99 - Count Collisions on a Road

**Problem Link**: [LeetCode 2211 - Count Collisions on a Road](https://leetcode.com/problems/count-collisions-on-a-road/)  
**Difficulty**: Medium

## Approach

We solve this with a **simple yet brilliant observation**:

> Cars going **left (`L`)** from the **left side** will never collide.  
> Cars going **right (`R`)** from the **right side** will never collide.

All other cars **will eventually collide** and stop.

### Key Insight:
- Remove all leading `'L'` → these cars are going left from the leftmost position → no one to hit.
- Remove all trailing `'R'` → these cars are going right from the rightmost position → no one to hit.
- After trimming:
  - Every `'L'` will hit something (a stopped car or an `'R'`)
  - Every `'R'` will hit something (a stopped car or an `'L'`)
- So **total collisions = number of remaining `'L'` + `'R'`**

### Steps:
1. `directions.lstrip('L')` → remove all cars going left from the left
2. `directions.rstrip('R')` → remove all cars going right from the right
3. Count remaining `'L'` and `'R'` → each contributes **exactly one collision**
4. Return sum

### Example: `"RLRSLL"`
- Original: `R L R S L L`
- After `lstrip('L')` → `"RLRSLL"` (no change)
- After `rstrip('R')` → `"RLRSLL"` → still no change
- Remaining: 2 `'R'` + 2 `'L'` → **4 collisions**

Actually:  
→ `"RRRSLL"` → after trimming → `"RRSLL"` → 2R + 2L = 4 → correct!

### Example: `"LLRR"` → after `lstrip('L')` and `rstrip('R')` → `""` → 0 collisions → correct!

## Complexity

- **Time**: **O(n)**
- **Space**: **O(1)** (if we modify string in-place, otherwise O(n))

## Screenshot
![Solution Screenshot](screenshot.png)