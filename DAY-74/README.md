# Day 74 - Count Operations to Obtain Zero

**Problem Link**: [LeetCode 2169 - Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero/)  
**Difficulty**: Easy

## Approach

We solve this by **simulating** the subtraction process until one number becomes zero.

- Initialize `res = 0` to count operations.
- While **both** `num1` and `num2` are greater than 0:
  - Subtract the **smaller** number from the **larger** one.
  - Increment `res` by 1.
- Return `res` — total number of subtractions.

> This is essentially the **Euclidean algorithm** in disguise (but using subtraction instead of modulo).

### Why it works:
- Each subtraction reduces the larger number.
- Eventually, one number becomes zero.
- The number of steps is **exactly** what the problem asks for.

> Example: `num1 = 5`, `num2 = 3`  
> - `5 - 3 = 2` → `res = 1`  
> - `3 - 2 = 1` → `res = 2`  
> - `2 - 1 = 1` → `res = 3`  
> - `1 - 1 = 0` → `res = 4`  
> → **4 operations**

## Complexity

- **Time**: **O(max(num1, num2))** — worst case: subtract 1 repeatedly
- **Space**: **O(1)** — only a few variables

## Screenshot
![Solution Screenshot](screenshot.png)