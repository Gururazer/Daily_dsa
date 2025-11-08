# Day 73 - Minimum One Bit Operations to Make Integers Zero

**Problem Link**: [LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)  
**Difficulty**: Hard

## Approach

We solve this using a **clever bit manipulation trick** based on the observation that:

> **The minimum number of operations to reduce `n` to `0` is equal to the XOR of all numbers obtained by right-shifting `n` until it becomes zero.**

### Step-by-step:
- Initialize `opts = 0`
- While `n > 0`:
  - XOR `opts` with current `n`
  - Right-shift `n` by 1 (`n >>= 1`)
- Return `opts`

### Why it works:
- Each right shift corresponds to removing the least significant bit.
- The XOR accumulates the cost of flipping bits in a way that cancels out overlapping operations.
- This turns out to be the **exact minimum** due to the problem’s unique operation rules.

> Example: `n = 5 (101)`  
> `opts = 0`  
> - `opts ^= 5` → `101`  
> - `n = 2 (10)`  
> - `opts ^= 2` → `101 ^ 010 = 111`  
> - `n = 1 (1)`  
> - `opts ^= 1` → `111 ^ 001 = 110` → **6**  
> → Correct!

## Complexity

- **Time**: **O(log n)** — number of bits in `n`
- **Space**: **O(1)** — only one variable

## Screenshot
![Solution Screenshot](screenshot.png)