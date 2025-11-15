# Day 80 - Count the Number of Substrings With Dominant Ones

**Problem Link**: [LeetCode 3234 - Count the Number of Substrings With Dominant Ones](https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/)  
**Difficulty**: Hard

## Approach

We solve this using **two-pointer + precomputed next zero index** to count valid substrings where `ones² > zeros`.

### Key Insight:
> For a substring to have **dominant ones**, we need:  
> `count_1s² > count_0s`

We fix the **number of zeros** (`z`) and find **valid ranges** of `1`s.

---

### Steps:

1. **Precompute `nextz[i]`**:
   - `nextz[i]` = index of **next `'0'`** starting from `i+1`, or `n` if none.
   - Enables **O(1)** jumps to next zero.

2. **Iterate over left endpoint `l`**:
   - Start with `zeroes = 0` (or 1 if `s[l] == '0'`)
   - `r = l`
   - While `zeroes * zeroes <= n`:
     - Jump to next zero: `nxtz = nextz[r]`
     - Count `ones = (nxtz - l) - zeroes`
     - If `ones >= zeroes * zeroes`:
       - Valid ones range: `[zeroes², ones]`
       - Can extend right up to `nxtz - 1`
       - Add: `min(nxtz - r, ones - zeroes² + 1)`
     - Move `r = nxtz`, `zeroes += 1`

> This counts **all substrings** with exactly `z` zeros and sufficient ones.

---

## Complexity

- **Time**: **O(n √n)** — `zeroes` up to `√n`, and we jump over zeros
- **Space**: **O(n)** — for `nextz` array

## Screenshot
![Solution Screenshot](screenshot.png)